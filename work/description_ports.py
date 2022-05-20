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
    cur.execute("SELECT acctstoptime,vremyazvonka,komu_zvonyat,kto_zvonit FROM `radacct` WHERE (acctstoptime>'2022-05-01 00:00:00' AND acctstoptime<'2022-07-01 10:00:00') ORDER BY acctstoptime")
    rows = cur.fetchall()
    for row in rows:
        print(row)
        # if row['ip_number']==1096:
        #     print('Нашли, вот его имя=', row["name_phone"], ', и вот его телефон =', row["id_phone"])
        # else:
        #     continue
