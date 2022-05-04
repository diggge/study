#!/usr/bin/python3
# -*- coding: utf-8 -*-
import pymysql.cursors
con = pymysql.connect(host='10.77.3.24',
                      user='ivanov-aa',
                      password='Ctynz,hm2',
                      db='baza_se',
                      charset='utf8mb4',
                      cursorclass=pymysql.cursors.DictCursor)
with con:
    cur = con.cursor()
    cur.execute("SELECT * FROM `TABLE 1`")
    rows = cur.fetchall()
    for row in rows:
        # print(row["ip_number"], row["name_phone"], row["id_phone"])
        if row['ip_number']==1096:
            print('Нашли, вот его имя=', row["name_phone"], ', и вот его телефон =', row["id_phone"])
        else:
            continue
