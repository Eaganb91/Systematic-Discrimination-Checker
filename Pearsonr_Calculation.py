import pandas as pd
import numpy
from scipy.stats import pearsonr

#Sample data
data = {
  "Age": [42, 38, 39, 26, 21, 63, 28],
  "Salary": [70000, 65000, 63500, 60000, 55000, 66000, 65000]
}

df = pd.DataFrame(data)

correlation, pValue = pearsonr(df["Age"], df["Salary"])
print(f"{correlation:.2f}")
print(f"{pValue:.2f}")