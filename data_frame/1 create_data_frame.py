
# What is a DataFrame in Pandas? (English)

# A DataFrame is a 2-dimensional tabular data structure in Pandas.

# 👉 It looks like an Excel sheet or SQL table.
# 👉 It has rows and columns.

# A DataFrame can store:

# Numbers
# Strings
# Dates
# Mixed data typesWhat is a DataFrame in Pandas? (English)

# A DataFrame is a 2-dimensional tabular data structure in Pandas.

# 👉 It looks like an Excel sheet or SQL table.
# 👉 It has rows and columns.

# A DataFrame can store:

# Numbers
# Strings
# Dates
# Mixed data types



# Pandas DataFrame kya hota hai? (Hindi)

# DataFrame Pandas ka sabse important data structure hai.

# 👉 Ye rows aur columns me data store karta hai.
# 👉 Isse Excel sheet ya database table ki tarah samajh sakte ho.



import numpy as np
import pandas as pd

# data = {
#     "Name": ["Arshad", "Ali", "Rahul"],
#     "Age": [22, 25, 24],
#     "city":["kushinagar","delhi","gorakhpur"],
#     "salary":[2344,5654,7876]
# }

# df=pd.DataFrame(data)
# print(df)
data2=[["asddd",2344,"q3rq3r4",987],
        ["sdf",23344,"q3rq3r4",9857],
        ["hbf",23464,"q3rq3r4",9877],
        ["jl",23744,"q3rq3r4",9587]]
col=["Name", "salary", "n","s"]
df2=pd.DataFrame(data2,columns=col)

# Selection columns

df2["Name"]
# print(df2["Name"])
# print(df2[["Name","salary"]])

# create a new column

df2["roll"]=["werfvf","erfss","rtfdhr","uytrtyu"]
# print(df2)

# Delete data column

# df2.drop("roll",axis=1,inplace=True)




# selection row

# df2.loc(0)
# print(df2.loc[0])
# p=df2.loc[[0,1]]
# print(p)


# selction a spacific part
p2=df2.loc[[0,1]][["n","s"]]
# print(p2)


# Condition selection(+,-,*,/,=,<,>)


p3=df2[(df2["Name"]=="sdf") & (df2["salary"]>2334)]
print(p3)

