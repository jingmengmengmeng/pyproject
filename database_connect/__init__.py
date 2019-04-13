import os
import pymysql
fo = open("foo.txt", "r+")
str = fo.read(10)
print("字符串是 : ", str)

fo.close()


os.rename("AA.txt","test.txt")