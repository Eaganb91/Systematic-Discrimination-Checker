import pandas as pd
import random
from scipy.stats import pearsonr

import pandas as pd

#returns a data frame that it generates from asking the user questions
def createData(numEmployee=None,pay=None,payVariance=None,age=None,ageVariance=None,ageCorrelation=None,correlationVariance=None,genderRatio=50,isImigrantRatio=10,phyisicalDisabilityRatio=5,neurodivergentRatio=10,recordOfOffences=5,years=5,yearsVariance=4,performanceAverage=7,performanceVariance=3):
    header=["id","pay","jobTitle","yearsAtCompany","hiredBy","promotedLastBy","performanceMetric","age","gender","isImmigrant","physicalDisability","neurodivergent","recordOfOffences"]
    dtypes = {
        "id": 'Int64',               # Use nullable Int64 for integers
        "pay": float,
        "jobTitle": 'string',        # Use dedicated Pandas string type
        "yearsAtCompany": 'Int64',
        "hiredBy": 'string',
        "promotedLastBy": 'Int64',
        "performanceMetric": float,  # Added the missing column
        "age": 'Int64',
        "gender": 'Int64',
        "isImmigrant": 'Int64',
        "physicalDisability": 'Int64',
        "neurodivergent": 'Int64',
        "recordOfOffences": 'Int64'
    }
    data=pd.DataFrame(columns=header).astype(dtypes)
    if(numEmployee is None):
        numEmployee=int(input("enter the number of employess in this company: "))
    if(pay==None):
        pay=int(input("enter a average salarie: "))
    if(payVariance==None):
        payVariance=int(input("enter a pay variance: "))
    if(age==None):
        age=int(input("enter an average age"))
    if(age==None):
        ageVariance=int(input("enter variance for age"))
    if(ageCorrelation==None):
        ageCorrelation=float(input("enter the correlation between age and pay"))
    if(correlationVariance==None):
        correlationVariance=int(input("enter how concistent the correlation is out of 100"))
    numPromoters=4
    numManage=10
    #formula for pay change is going to be newPay=pay*(mean(age)-age)*ageCorrelation*correlationVariance
    print("generating", numEmployee, "employees")

    for i in range(numEmployee):
        if numManage>0:
            manage=1
            numManage=numManage-1
        else:
            manage=0
        #seed=random.randint(1,100)
        
        new_row_df = pd.DataFrame([createEmployee(i, pay-random.randint(-payVariance,payVariance),manage,years+random.randint(-yearsVariance,yearsVariance),None,random.randint(0,numPromoters),performanceAverage+random.randint(-performanceVariance,performanceVariance),age+random.randint(-ageVariance,ageVariance),pick(genderRatio),pick(isImigrantRatio),pick(phyisicalDisabilityRatio),pick(neurodivergentRatio),pick(recordOfOffences))], columns=data.columns)
        data = pd.concat([data, new_row_df], ignore_index=True)
        data.loc[i,"pay"]=data.loc[i,"pay"]-((age-data.loc[i,"age"])*ageCorrelation*random.randint(0,correlationVariance)/100)
    print(data)
    return data
def pick(ratio):
    seed=random.randint(1,100)
    if(seed>ratio):
        return 0
    else:
        return 1
#creates an employee as a array and returns it
#employeeNumber	pay	yearsAtCompany	hiredBy	promotedLastBy	performanceMetric	age	gender	isImmigrant	physicalDisability	neurodivergent	recordOfOffences
def createEmployee(id=None,pay=None,jobTitle=None,yearsAtCompany=None,hiredBy=None,promotedLastBy=None,performanceMetric=None,age=None,gender=None,isImmigrant=None,physicalDisability=None,neurodivergent=None,recordOfOffences=None):
    return[id,pay,jobTitle,yearsAtCompany,hiredBy,promotedLastBy,performanceMetric,age,gender,isImmigrant,physicalDisability,neurodivergent,recordOfOffences]

def checkCorrelation(df, col1, col2):
    correlation, pValue = pearsonr(df[col1], df[col2])

    #NEW convert columns to numeric, coerce errors to NaN
    x = pd.to_numeric(df[col1], errors='coerce')
    y = pd.to_numeric(df[col2], errors='coerce')

    #NEW - drop NaNs from both
    mask = x.notna() & y.notna()
    x_clean = x[mask]
    y_clean = y[mask]

    #NEW
    if len(x_clean) < 2:
        print(f"Not enough valid data to compute correlation between {col1} and {col2}")
        return None, None, col1, col2
    
    correlation, pValue = pearsonr(x_clean, y_clean)

    #print(f"{correlation:.2f}")
    #print(f"{pValue:.2f}")
    return correlation, pValue,col1,col2

def printCorrelation(correlation,pValue,col1,col2):
    RED = '\033[91m'
    GREEN = '\033[92m'
    RESET = '\033[0m'
    #print(correlation,pValue)
    if(pValue>0.05):
        print(f"{GREEN}there is no correlation at a 95 percent confidence interval between {col1} and {col2}{RESET}")
    else:
        print(f"{RED}there is evidence there is a correlation between {col1} and {col2}{RESET}")
    print("")


def compareProtected(df,correlator):
    printCorrelation(*(checkCorrelation(df,correlator,"age")))
    printCorrelation(*(checkCorrelation(df,correlator,"gender")))
    printCorrelation(*(checkCorrelation(df,correlator,"isImmigrant")))
    printCorrelation(*(checkCorrelation(df,correlator,"physicalDisability")))
    printCorrelation(*(checkCorrelation(df,correlator,"neurodivergent")))
    printCorrelation(*(checkCorrelation(df,correlator,"recordOfOffences")))


def checkPromoter(df):
    promoters=df['promotedLastBy'].tolist()
    promoters=set(promoters)
    for p in promoters:
        dfCopy =df.copy(deep=True)
        # 1. Select the column and set all values to 0
        dfCopy['promotedLastBy'] = 0

        # 2. Use .loc to select only the rows where the original value *was* 'p' 
        #    and set the corresponding new value to 1
        dfCopy.loc[df['promotedLastBy'] == p, 'promotedLastBy'] = 1
        print("checking if employer",p,"has systematic bias in there promotion decisions")
        compareProtected(dfCopy,"promotedLastBy")
    

def createCorrelation(df):
    print("this function will change peoples pay bassed on an inputed protected class to simulate systemic discrimination")
    y="pay"

    strength=float(input("enter the strength of the correlation. 1 is maximumly strong"))
    print("These are you'r options for what to have as a independent variable for the correleation:")
    print("1. Age")
    print("2. gender")
    print("3. isImmigrant")
    print("4. physicalDisability")
    print("5. neurodivergent")
    print("6 record of offenses")
    xInput=int(input("enter the number: "))
    x=["age","gender","isImmigrant","physicalDisability","neurodivergent","recordsOfOffences"][xInput-1]
    variance=int(input("enter the variance of the correlation. enter 0 for no variance"))
    base_effect = df[y].abs().mean() * strength
    df[y]=df[y]+df[x]*base_effect
    print(df)
    return df

def displayComanyInfo(file):
    ##COMPANY INFO
    
    #avg finders
    meanAge = file["age"].mean()
    meanTenure = file["yearsAtCompany"].mean()

    #National Compare
    medianPay = file["pay"].median()
    womanSum = (file["gender"] == 1).sum()
    genderSum = len(file["gender"])
    femaleProportion = ((womanSum / genderSum) * 100)
    #print(f"Gender Split {womanDistribution:.2f}%")

    avgPayMen = file.loc[file["gender"] == 1, "pay"].mean()
    avgPayWomen = file.loc[file["gender"] == 0, "pay"].mean()

    payGap = ((avgPayMen - avgPayWomen) / avgPayMen) * 100

    #display info
    print("COMPANY INFORMATION:")
    print("------------------------------------------")
    print("Proportion of protected classes breakdown:")
    mentalDisabilityCounter = (file["neurodivergent"] == 1).sum()
    mentalDisabilityProportion = (mentalDisabilityCounter / genderSum) * 100
    print(f"Mental Disability: {mentalDisabilityProportion:.2f}%")

    physicalDisabilityCounter = (file["physicalDisability"] == 1).sum()
    physicalDisabilityProportion = (physicalDisabilityCounter / genderSum)
    print(f"Physical Disability: {physicalDisabilityProportion:.2f}%")

    offencesCounter = (file["recordOfOffences"] == 1).sum()
    criminalProportion = (offencesCounter / genderSum) * 100
    print(f"Record of Offences: {criminalProportion:.2f}%")

    immigrantCounter = (file["isImmigrant"] == 1).sum()
    immigrantProportion = (immigrantCounter / genderSum) * 100
    print(f"Immigrant Proportion: {immigrantProportion:.2f}%")
    print("------------------------------------------")
    return femaleProportion, medianPay, payGap


    
## NATIONAL COMPARE
def industryCompare(femaleProportion, medianPay, payGap):
    # dictionary to hold industry values
    industryValues = {
        "Agriculture, forestry, fishing, hunting, mining, quarrying, oil and gas extraction, and utilities": [24.1, 40.00, 9.3],
        "Construction": [14.5, 32.00, 14.5],
        "Manufacturing": [29.4, 27.50, 12.5],
        "Wholesale trade": [33.2, 28.90, 10.2],
        "Retail trade": [50.8, 20.00, 16.0],
        "Transportation and warehousing": [26.8, 28.20, 12.4],
        "Information and cultural industries": [42.6, 31.70, 11.6],
        "Finance and insurance": [55.0, 36.10, 20.5],
        "Real estate and rental and leasing": [47.0, 28.30, 11.9],
        "Professional, scientific and technical services": [44.9, 36.90, 19.7],
        "Educational services": [71.9, 36.60, 10.1],
        "Health care and social assistance": [82.9, 28.00, 6.2],
        "Accommodation and food services": [55.8, 17.50, 8.7],
        "Admin, support, waste management, remediation, and other services": [45.8, 23.10, 7.6],
        "Public administration": [50.3, 40.00, 7.8]
    }
    # function to print if your company does/does not beat national average
    def resultPrint(diff: float, metric_name: str):
        RED = "\033[91m"
        GREEN = "\033[92m"
        RESET = "\033[0m"
        if diff > 0:
            print(f"{GREEN}Your company has a higher {metric_name} than the industry average.{RESET}")
        elif diff == 0:
            print(f"Your company has a {metric_name} on par with the industry average.")
        else:
            print(f"{RED}Your company has a lower {metric_name} than the industry average.{RESET}")

    # create a hashmap to link user choice to specific industry
    industryHashMap = {}
    for i, name in enumerate(industryValues.keys()):
        industryHashMap[i + 1] = name

    print("----------------------------------------------------------------------------------------------------")
    for key, i in industryHashMap.items():
        print(f"{key}. {i}")
    print("----------------------------------------------------------------------------------------------------")

    while True:
        try:
            selectIndustry = int(input("\nPlease enter the associated int value of the value you would like to compare to (enter '-1' to skip): "))
        except ValueError:
            print("Please only enter int values (0-9)")
            continue

        if selectIndustry in industryHashMap:
            comparedIndustry = industryHashMap[selectIndustry]
            values = industryValues[comparedIndustry]
            print("\n" + comparedIndustry)
            print("           Proportion of Women - Median Hourly Wage - Pay Gap\n")

            print("Industry:", end=" ")
            print(f"{values[0]:>14.2f}% ", end="")
            print(f"{values[1]:>18.2f}$ ", end="")
            print(f"{values[2]:>13.2f}$ ", end="")

            print("\nYour Company:", end=" ")
            print(f"{femaleProportion:>10.2f}% ", end="")
            print(f"{medianPay:>18.2f}$ ", end="")
            print(f"{payGap:>13.2f}$ ", end="")

            distDiff = femaleProportion - values[0]
            payDiff = medianPay - values[1]
            gapDiff = payGap - values[2]

            print("\n\nResults:")
            resultPrint(distDiff, "proportion of females")
            resultPrint(payDiff, "median pay")
            resultPrint(gapDiff, "gender pay gap")
            print("----------------------------------------------------------------------------------------------------")

        if selectIndustry == -1:
            break 


#numEmployee=None,pay=None,payVariance=None,age=None,ageVariance=None,ageCorrelation=None,correlationVariance=None
def main():
    while True:
        tableData = input("Do you want to generate test data or input a preexisting file?Y/N: ")
        try:
            if tableData == "Y":
                df = createData(1000,100,10,30,10,0,100)
                break
            elif tableData == "N":
                #filePath = input("Enter the file path to a csv file").strip()
                #df = pd.read_csv(filePath)
                filePath = input("Enter the file path to a csv file").strip()
                filePath = filePath.replace("\\", "/")
                df = pd.read_csv(filePath)
                break
        except ValueError:
            print("Enter Y for test data, enter N to input your own file: ")
    while True:
        print("1. Check for corellation's between pay and things protected class's in Ontario human rights law")
        print("2. Check for corellation's between promoters on things protected class's in Ontario human rights law")
        print("3. Creates a correlation in the test data")
        print("4. print's out the data")
        print("5. print out the companies employment proportion of protected classes")
        print("6. compare the companies data to Canadian industry benchmarks")
        print("7. exit application")
        compare = int(input("Enter your input: "))
        if compare==1:
            #print out the wether each function has a correlation
            print("checking everything for comparison")
            compareProtected(df,"pay")
        if compare==2:
            print("checking each employee in charged of promoting for bias's")
            checkPromoter(df)
        if compare==3:
            df=createCorrelation(df)
        if compare==4:
            print(df)
        if compare ==5:
            displayComanyInfo(df)
        if compare == 6:
            femaleProportion, medianPay, payGap = displayComanyInfo(df)
            industryCompare(femaleProportion, medianPay, payGap)
        if compare == 7:
            break

main()