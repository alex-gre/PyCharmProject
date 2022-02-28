import sqlite3

import pandas


connection = sqlite3.connect('organizer.db')

df = pandas.read_csv('organizer.csv', sep=',')
df.to_sql('organizer', connection, if_exists='append', index=False)