#
# atten.py
# Developer:GUOCHENYU
# 2022/5/8
import datetime
import pandas as pd
import numpy as np
import pymysql
from MySql import AttenTime

n=datetime.datetime.now()
b=datetime.datetime(n.year,n.month,n.day,9,0,0)
q=n-b
print(q)
if n>b:
    print("a")
else:
    print("c")
print(n)
print(b)
conn=pymysql.connect(host='localhost',port=3306,user='guo',passwd='123456',db='employee',charset='utf8mb4')
cursor=conn.cursor()

a=AttenTime('q')



conn.commit()
a.close()
# 使用pandas的read_sql_query函数执行SQL语句，并存入DataFrame
#df_read = pd.read_sql_query(sql_query, conn)
#print(df_read)

#print(time)time=datetime.datetime.now().strftime("%Y-%m-%d%H:%M:%S")


#sql='time'
#pid='startTime'
#sid= "guochenyu"
#print(id)
#sql_query = "UPDATE runoob_tbl SET runoob_title='学习 C++' WHERE runoob_id=3;"

#cursor.execute(sql_query, (sid, pid, time)) #添加参数
