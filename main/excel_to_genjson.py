import pandas as pd




df = pd.read_excel(r'C:\Users\李缉\Desktop\ST-MapMatching-main\data\excel\traj_21.xlsx')#默认读取工作簿中第一个工作表，默认第一行为表头
data=df.values#获取整个工作表数据


data=df.iloc[0,1]#读取索引为[1, 2]的值，这里不需要嵌套列表
print("读取指定某行某列（单元格）的数据：\n{0}".format(data))

# print("读取整个工作表的数据：\n{0}".format(data))
# data=df.iloc[0].values#0表示第一行，不包含表头
# print("读取指定行的数据：\n{0}".format(data))
# data=df.head().values#head()默认读取前5行数据（不包含表头）
# print("获取工作表前5行数据:\n{0}".format(data))
#
# data=df.iloc[[1,2]].values#读取指定多行，在iloc[]里面嵌套列表指定行数
# print("读取指定多行的数据：\n{0}".format(data))
#
# data=df.sample(3).values#读取df中随机3行数据(3个样本）
# print("获取随机多行数据:\n{0}".format(data))





# # 读取csv文件
# import csv
# with open('test.csv','r') as myFile:
#     lines=csv.reader(myFile)
#     for line in lines:
#         print (line)

# file1 = open('./data/excel/traj_21.csv', 'r', encoding='utf-8')
# transformer = file1.read()
# print(transformer)
# file1.close()
#
# import csv
#
# with open('./data/excel/traj_21.csv', 'r', encoding='utf-8') as file:
#     file1 = csv.reader(file)
#     for files in file1:
#         print(files)
# import numpy as np
# import xlrd
#
# def create_data(path1):
#     table1 = xlrd.open_workbook(path1).sheets()[0]  # 获取第一个sheet表
#     row1 = table1.nrows  # 行数
#     col1 = table1.ncols  # 列数
#