import pandas as pd

'''
file = pd.read_csv(r'c:\Users\2gavi\Downloads\example company spredsheet - Sheet1.csv')
print(file.head())

#avg finders
meanAge = file["age"].mean()
meanTenure = file["yearsAtCompany"].mean()

#National Compare

medianPay = file["pay"].median()

womanSum = (file["gender"] == "W").sum()
genderSum = len(file["gender"])
womanDistribution = ((womanSum / genderSum) * 100)


print(f"Gender Split {womanDistribution:.2f}%")

avgPayMen = file.loc[file["gender"] == "M", "pay"].mean()
avgPayWomen = file.loc[file["gender"] == "W", "pay"].mean()

payGap = ((avgPayMen - avgPayWomen) / avgPayMen) * 100
'''




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

industryHashMap = {i+1: name for i, name in enumerate(industryValues.keys())}

for key, industry in industryHashMap.items():
    print(f"{key}. {industry}")

while True:
    selectIndustry = int(input("\nPlease enter the associated int value of the value you would like to compare to (enter '-1' to skip):"))
    if selectIndustry in industryHashMap:
        counter = 0
        comparedIndustry = industryHashMap[selectIndustry]
        values = industryValues[comparedIndustry]
        
        print(comparedIndustry)
        print("                 Proportion of Women - Median Hourly Wage - Pay Gap\n")
        print("Industry:", end = " ")
        for i in values:
            print(f"{values[counter]:.2f} ", end = "")
            counter +=1

        print("\nYour Company:", end = " ")
        
        print(f"{womanDistribution:.2f}% ", end ="")
        print(f"{medianPay:.2f}$ ", end = "")
        print(f"{payGap:.2f}$ ", end ="")

    

    if selectIndustry == -1:
        break
    
    



#(f"Please Select the Canadian industry you would like to compare against \n1. Agriculture, forestry, fishing, hunting, mining, quarrying, oil and gas extraction, and utilities\n2. Construction\n3. Manufacturing\n4. Wholesale trade\n5. Retail trade\n6. Transportation and warehousing\n7. Information and cultural industries\n8. Finance and insurance\n9. Real estate and rental leasing\n10. Professional, scientific, and technical services\n11. Educational services\n12. Health care and social assistance\n13. Accommodation and food services\n14. Admin, support, waste management, remediation, and other services\n15. Public administration")
