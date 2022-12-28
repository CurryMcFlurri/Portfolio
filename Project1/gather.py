import sqlite3
import pandas as pd
import matplotlib.pyplot as plt


dataset = pd.read_csv('DNase.csv')
#print(dataset)

#Creates data plot
#dataset.plot()
#plt.show()


conn = sqlite3.connect('dnaseinfo.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Assays')
cur.execute('''CREATE TABLE IF NOT EXISTS Assays 
(id INTEGER PRIMARY KEY, Run INTEGER, Conc TEXT, Density TEXT)''')

for row in dataset.itertuples():
   #print(row.Run, row.conc, row.density)
   
    cur.execute('''INSERT INTO Assays (run, Conc, Density) VALUES (?, ?, ?)''',
    (row.Run, row.conc, row.density))
conn.commit()