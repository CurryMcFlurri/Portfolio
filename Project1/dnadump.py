import matplotlib.pyplot as plt
import sqlite3
import pandas as pd

#Creates data plot
dataset = pd.read_csv('DNase.csv')
dataset.plot()
plt.show()

conn = sqlite3.connect('dnaseinfo.sqlite')
cur = conn.cursor()

con1 = list()
con2 = list()
con3 = list()
con4 = list()
con5 = list()
con6 = list()
con7 = list()
con8 = list()
#concentrations = dict()

cur.execute('SELECT Conc, Density FROM Assays')

for row in cur:
    #print(row)
    if row[0] == '0.04882812':
        con1.append(row[1])
    elif row[0] == '0.1953125':
        con2.append(row[1])
    elif row[0] == '0.390625':
        con3.append(row[1])
    elif row[0] == '0.78125':
        con4.append(row[1])
    elif row[0] == '1.5625':
        con5.append(row[1])
    elif row[0] == '3.125':
        con6.append(row[1])
    elif row[0] == '6.25':
        con7.append(row[1])
    elif row[0] == '12.5':
        con8.append(row[1])

con1 = [float(x) for x in con1]
con2 = [float(x) for x in con2]
con3 = [float(x) for x in con3]
con4 = [float(x) for x in con4]
con5 = [float(x) for x in con5]
con6 = [float(x) for x in con6]
con7 = [float(x) for x in con7]
con8 = [float(x) for x in con8]
#print(type(con1[0]))
print('Average Density per Concentration Level:\n')
print('1:', sum(con1)/len(con1))
print('2:', sum(con2)/len(con2))
print('3:', sum(con3)/len(con3))
print('4:', sum(con4)/len(con4))
print('5:', sum(con5)/len(con5))
print('6:', sum(con6)/len(con6))
print('7:', sum(con7)/len(con7))
print('8:', sum(con8)/len(con8))

#print('1st concentation level: \n', con1, '\n')
#print('2nd concentation level: \n', con2, '\n')