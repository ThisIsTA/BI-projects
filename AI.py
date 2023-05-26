from mysql.connector import errorcode
import mysql.connector
from sklearn import tree
import re

cnx = mysql.connector.connect(host= "localhost", user= "root", password="09142229277t", database= "mainDB")
cursor = cnx.cursor()

DB_name = 'Used_Cars_Price_and_Miles'
#cursor.execute("USE {}".format(DB_name))
cursor.execute("SELECT * FROM car")

def con_int(n):
    res = re.sub("\D", "", n)
    return int(res)

def con_list(tpl):
    return list(tpl)

res = cursor.fetchall()

x = []
y = []

for row in res:
    row = con_list(row)
    for i in range(len(row)):
            row[i] = con_int(row[i])
    x.append(row[1:3])
    y.append(row[0])

clf = tree.DecisionTreeClassifier()
clf = clf.fit(x, y)

car = [['2020', '25000']]
answer = clf.predict(car)
print(answer)