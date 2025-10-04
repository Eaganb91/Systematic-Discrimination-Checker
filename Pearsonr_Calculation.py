import pandas as pd
import numpy
from scipy.stats import pearsonr

#Sample data
data = {
  "Age": [42, 38, 39, 26, 21, 63, 28],
  "Salary": [70000, 65000, 63500, 60000, 55000, 66000, 65000]
}

df = pd.DataFrame(data)

def checkCorrelation(df, col1, col2):
    correlation, pValue = pearsonr(df[col1], df[col2])
    print(f"{correlation:.2f}")
    print(f"{pValue:.2f}")
    return correlation, pValue
