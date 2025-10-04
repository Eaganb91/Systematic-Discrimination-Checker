import pandas as pd


file = pd.read_csv(r'thedownloadedgoogleSheetsfile.csv')
print(file.head())

#avg finders
meanAge = file["age"].mean()
meanTenure = file["yearsAtCompany"].mean()

#National Compare

medianPay = file["pay"].median()

womanSum = (file["gender"] == "W").sum()
genderSum = len(file["gender"])
womanDistribution = (womanSum / genderSum) * 100


avgPayMen = file.loc[file["gender"] == "M", "pay"].mean()
avgPayWomen = file.loc[file["gender"] == "W", "pay"].mean()

payGap = ((avgPayMen - avgPayWomen) / avgPayMen) * 100


