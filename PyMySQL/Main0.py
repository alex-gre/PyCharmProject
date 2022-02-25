#!/usr/bin/python3
# -*- coding: utf-8 -*-
# print version
import pymysql

con = pymysql.connect(host='localhost', user='user255', password='qwerty', db='employees')

with con:
    cur = con.cursor()
    cur.execute("SELECT VERSION()")

    version = cur.fetchone()

    print("Database version: {}".format(version[0]))
