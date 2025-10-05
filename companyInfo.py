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
womanDistribution = ((womanSum / genderSum) * 100)
#print(f"Gender Split {womanDistribution:.2f}%")

avgPayMen = file.loc[file["gender"] == "M", "pay"].mean()
avgPayWomen = file.loc[file["gender"] == "W", "pay"].mean()

payGap = ((avgPayMen - avgPayWomen) / avgPayMen) * 100
