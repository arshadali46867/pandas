# What is a Pandas Series? (English)

# A Pandas Series is a one-dimensional labeled array that can store data of any type (integers, strings, floats, etc.).

# 👉 Think of it as a single column of data in an Excel sheet.

# 🔹 Example
# import pandas as pd

# s = pd.Series([10, 20, 30, 40, 50])

# print(s)

# Output:

# 0    10
# 1    20
# 2    30
# 3    40
# 4    50

# Pandas Series kya hoti hai? (Hindi)

# Pandas Series ek 1-dimensional data structure hai jo data ko index ke saath store karti hai.





import numpy as np
import pandas as pd


labels=["a","b","c"]
list=[1,2,3]
arr=np.array([4,5,6])
dic={1:10,2:20,3:30}

# l=pd.Series(labels)
# l=pd.Series(list)
# l=pd.Series(arr)
l=pd.Series(dic)

# l=pd.Series(list,index=labels)



print(l)