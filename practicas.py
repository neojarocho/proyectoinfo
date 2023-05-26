e = 13
x = 5
y = 13
suma = x + y

t = "nani es bonita"
t[0:4]
t[8:14]

n = t[0:4]
b = t[8:14]

""" AND """

True and True
True and False
False and True 
False and False

""" OR """
True or True
True or False
False or True 
False or False


a = [2, "tres", True, ["uno", 10]]

a[0]
a[1]
a[1][0:1]


import pandas as pd

data = pd.DataFrame({'Pais': ['Belgica', 'India', 'Brasil'], 'Capital': ['Bruselas', 'Nueva Deli', 'Brasília'], 'Poblacion': [11190846, 1303171035, 207847528]})

dt =pd.DataFrame({
    'nombres':['Ivan','Mateo','Xela','Ana','Paola'],
    'edad':[43,2,14,13,13],
    'signos':['Aries','Caprirnio','Tauro','Virgo','Sagitario'],
    'Pasatiempos':['Leer','Morder','Acosar','Estudiar','Dormir']
    })
dt.iloc[4,0]

r = 3 + 2 # r es 5
r = 4 – 7 # r es -3
r = -7 # r es -7
r = 2 * 6 # r es 12
r = 2 ** 6 # r es 64
r = 7.0 / 2 # r es 3.5
r = 7 // 2 # r es 3.0
r = 7 % 2 # r es 1


import math as m

a = m.sqrt(25)

#importing the os module
import os

#to get the current working directory
os.getcwd()

# pip3 or conda to install openpyxl


# Read the Excell file
import pandas as pd

dt = pd.read_excel('data.xlsx')
print(dt)

dt[dt['signo'] == 'aries']

import pandas as pd

# Read the CSV file
dt = pd.read_csv('data.xlsx')

# View the first 5 rows
dt.head()



