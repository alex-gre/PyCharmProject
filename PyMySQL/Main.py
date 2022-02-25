#!/usr/bin/python3
# -*- coding: utf-8 -*-

import pymysql

con = pymysql.connect(host='localhost', user='user255', password='qwerty', db='employees')

with con:
    cur = con.cursor()
    cur.execute("SELECT * FROM employee_data")

    rows = cur.fetchall()

    for row in rows:
        print("{0} {1} {2} {3} {4} {5} {6} {7} {8}".format(row[0], row[1],
        row[2] ,row[3],row[4],row[5],row[6],row[7],row[8]))



