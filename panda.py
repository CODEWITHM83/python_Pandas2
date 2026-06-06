import pandas as pd
"""pandas Series (1-D) data Frame"""
# marks=pd.Series([85,90,75,92])
# print (marks)
""" You can also add Custom Index:"""
# marks=pd.Series([85,90],index=['Math','Science'])
# print(marks)
""" Pandas DataFrame(2-D)"""
# data={
#     'Name':['Milli','Noah','Mike'],
#     'Age':[21,22,20],
#     'Marks':[85,90,88]
# }
# df=pd.DataFrame(data)
# print(df)
"""Createing DataFrame from Dictionary"""
# data={
#     'Name':['Ram','Sham','Rohit','Mohit'],
#     'Age':[22,34,25,33],
#     'Salary':[30000,40000,340000,240000],
#     'Department':['HR','IT','Finance','IT']
# }
# df=pd.DataFrame(data)
# print(df)
""" Read  Data From CSV and EXCEL"""
df=pd.read_csv('output.csv')
"""Essential Commands:"""
"""View First/ Last Rows"""
# print(df.head(1)) 
# print(df.tail(2))
"""DataSet information"""
print(df.shape)