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
        "SELECT callingstationid,calledstationid,acctstarttime,acctsessiontime,nasipaddress FROM `history_phone` WHERE (acctstarttime>'2022-05-01 00:00:00' AND acctstoptime<'2022-07-01 10:00:00') ORDER BY acctstoptime")
    rows = cur.fetchall()
    for row in rows:
        if (row["callingstationid"] == '1096' or row["calledstationid"] == '1096'):
            print('Кто звонил: ', row["callingstationid"], 'Кому звонил:', row["calledstationid"], 'Время и Дата звонка:', row["acctstarttime"], 'Длительность звонка:', row["acctsessiontime"])
        # if row["calledstationid"] == '2510':
        #     print('На указанный номер звонили с номера: ', row["callingstationid"], 'Время и Дата звонка:', row["acctstarttime"], 'Длительность звонка:' ,row["acctsessiontime"])
        # elif row["callingstationid"] == '2510':

        #     print('Указанный номер звонил на номера: ', row["calledstationid"], 'Время и Дата звонка:', row["acctstarttime"], 'Длительность звонка:' ,row["acctsessiontime"])
        # # elif row["nasipaddress"] == '10.200.0.8':
        #
        #     pprint('Кто звонил: ', row["callingstationid"], 'Кому звонил',row["calledstationid"], 'Время и Дата звонка:', row["acctstarttime"], 'Длительность звонка:', row["acctsessiontime"])
        # else:
        #     print('Не нашли звонков')
        #      continue
