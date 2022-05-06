#!/usr/bin/python3
# -*- coding: utf-8 -*-
import pymysql.cursors
con = pymysql.connect(host='10.77.3.24',
                      user='ivanov-aa',
                      password='Ctynz,hm2',
                      db='radius',
                      charset='utf8mb4',
                      cursorclass=pymysql.cursors.DictCursor)
with con:
    cur = con.cursor()
    cur.execute("SELECT acctstoptime,vremyazvonka,komu_zvonyat,kto_zvonit FROM `radacct` WHERE (komu_zvonyat=2356 or kto_zvonit=2356) AND (acctstoptime>'2022-05-06 00:00:00' AND acctstoptime<'2022-07-01 10:00:00') ORDER BY acctstoptime")
    rows = cur.fetchall()
    for row in rows:
        print(row)
        # if row['komu_zvonyat']==2356:
        #      print('Нашли звонки=', row["acctstoptime"], row["vremyazvonka"], row["komu_zvonyat"], row["kto_zvonit"], row["acctstoptime"])
        #  else:
        #      continue
