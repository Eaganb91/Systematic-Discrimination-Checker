##CUT FROM NATIONAL COMPARE

import pandas as pd

#replace with entered file from above
import pandas as pd

#replace with entered file from above
file = pd.read_csv(r'C:\Users\2gavi\Downloads\example company spredsheet - Sheet1(2).csv')
print(file.head())

#avg finders
meanAge = file["age"].mean()
meanTenure = file["yearsAtCompany"].mean()

#National Compare
medianPay = file["pay"].median()
womanSum = (file["gender"] == "W").sum()
genderSum = len(file["gender"])
femaleProportion = ((womanSum / genderSum) * 100)
#print(f"Gender Split {womanDistribution:.2f}%")

avgPayMen = file.loc[file["gender"] == "M", "pay"].mean()
avgPayWomen = file.loc[file["gender"] == "W", "pay"].mean()

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


##CUT TO HERE


#dictionnary to hold industry values
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

#function to print if your company does/does not beat national average
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

#create a hasmap to link user choice to specific industry
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
        counter = 0
        comparedIndustry = industryHashMap[selectIndustry]
        values = industryValues[comparedIndustry]
        #control for string
        print("\n"+comparedIndustry)
        print("           Proportion of Women - Median Hourly Wage - Pay Gap\n")

        print("Industry:", end = " ")
        print(f"{values[0]:>14.2f}% ", end = "")
        print(f"{values[1]:>18.2f}$ ", end = "")
        print(f"{values[2]:>13.2f}$ ", end = "")

        print("\nYour Company:", end = " ")
        print(f"{femaleProportion:>10.2f}% ", end ="")
        print(f"{medianPay:>18.2f}$ ", end = "")
        print(f"{payGap:>13.2f}$ ", end ="")

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
    
    



#(f"Please Select the Canadian industry you would like to compare against \n1. Agriculture, forestry, fishing, hunting, mining, quarrying, oil and gas extraction, and utilities\n2. Construction\n3. Manufacturing\n4. Wholesale trade\n5. Retail trade\n6. Transportation and warehousing\n7. Information and cultural industries\n8. Finance and insurance\n9. Real estate and rental leasing\n10. Professional, scientific, and technical services\n11. Educational services\n12. Health care and social assistance\n13. Accommodation and food services\n14. Admin, support, waste management, remediation, and other services\n15. Public administration")
