import numpy as np
import pandas as pd

data={
    'A':[1,2,3,np.nan],
    'B':[4,12,34,np.nan],
    'C':[17,23,np.nan,45],
    'D':[76,34,67,88]


}
df=pd.DataFrame(data)
# print(df)
# p2=df.isna()
# p2=df.isna().sum()
# p2=df.isna().any()

# print(p2)

# removing missing data

# p3=df.dropna()
# p3=df.dropna(thresh=3)
# print(p3)
# print(df)

# filling missing data

p4=df.fillna(0)
values={'A':0,'B':400,'C':500,'D':600}
p4=df.fillna(values)
print(p4)
