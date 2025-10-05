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

