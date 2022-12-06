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
    cur.execute(
        "SELECT callingstationid,calledstationid,acctstarttime,acctsessiontime,nasipaddress FROM `history_phone` WHERE (acctstarttime>'2022-01-01 00:00:00' AND acctstoptime<'2022-12-31 23:00:00') ORDER BY acctstarttime")
    rows = cur.fetchall()
    for row in rows:
        if (row["callingstationid"] == '2369' or row["calledstationid"] == '2369'):
                    print('Кто звонил: ', row["callingstationid"], 'Кому звонил:', row["calledstationid"], 'Время и Дата звонка:', row["acctstarttime"], 'Длительность звонка:', row["acctsessiontime"])
        #     print('Указанный номер звонил на номера: ', row["calledstationid"], 'Время и Дата звонка:', row["acctstarttime"], 'Длительность звонка:' ,row["acctsessiontime"])
        # if row["nasipaddress"] == '10.200.0.8':
        #     print('Кто звонил: ', row["callingstationid"], 'Кому звонил',row["calledstationid"], 'Время и Дата звонка:', row["acctstarttime"], 'Длительность звонка:', row["acctsessiontime"])
    else:
        print('Не нашли звонков')
        #      continue
