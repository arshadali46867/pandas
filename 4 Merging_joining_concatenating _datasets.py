import numpy as np
import pandas as pd



students = pd.DataFrame({
    "ID": [1, 2, 3,4],
    "Name": ["Arshad", "Ali", "Rahul","gfxch"],
    "Age": [22, 23, 24,77],
    "City": ["Lucknow", "Delhi", "Mumbai","fghj"],
    "Course": ["Python", "Django", "Data Science","fdghj"]
})

marks = pd.DataFrame({
    "ID": [1, 2, 3,8],
    "Python": [85, 90, 78,76],
    "Django": [88, 92, 80,90],
    "SQL": [82, 89, 75,45],
    "Attendance": [95, 90, 85,87]
})

# print(students)
# print(marks)


p=pd.merge(students,marks)
        #   or
p=pd.merge(students,marks,on='ID')

p=pd.merge(students,marks,on='ID',how="inner")

p=pd.merge(students,marks,on='ID',how="outer")


p=pd.merge(students,marks,on='ID',how="left")


p=pd.merge(students,marks,on='ID',how="right")

# print(p)

# concatenation

import pandas as pd

df1 = pd.DataFrame({
    "ID": [1, 2, 3],
    "Name": ["Arshad", "Ali", "Rahul"]
})

df2 = pd.DataFrame({
    "ID": [4, 5, 6],
    "Name": ["Aman", "Vijay", "Rohit"]
})

result = pd.concat([df1, df2])
result = pd.concat([df1, df2],axis=1)

# print(result)



# Joining

import pandas as pd

df1 = pd.DataFrame({
    "Name": ["Arshad", "Ali", "Rahul"]
}, index=[1, 2, 3])

df2 = pd.DataFrame({
    "Marks": [85, 90]
}, index=[1, 2])

result = df1.join(df2, how="left")

print(result)


# groupby

df = pd.DataFrame({
    "Department": ["IT", "IT", "HR", "HR"],
    "City": ["Delhi", "Mumbai", "Delhi", "Mumbai"],
    "Salary": [50000, 60000, 40000, 45000]
})

# print(df.groupby(["Department", "City"])["Salary"].sum())


# Agregation
result = df.groupby("Department")["Salary"].agg(
    ["sum", "mean", "max", "min", "count"]
)

print(result)