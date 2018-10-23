#!/usr/bin/python
# -*- coding: UTF-8 -*-
import MySQLdb
import config
import csv

def insert_data(table,filename):
    try:
        conn = MySQLdb.connect(config.host, config.user, config.password)
        cur = conn.cursor()
        conn.select_db(config.databaseName)
    except MySQLdb.Error, msg:
        print "MySQL connet error %d: %s" % (msg.args[0], msg.args[1])
    out = open(filename,'r')
    # 循环插入
    while True:
        line=out.readline().strip('\n')
        if line:
            list=line.split(',')
            sql=("insert into "+table+" values(%s,%s,%s)")%tuple(list)
            print sql
            cur.execute(sql)
            conn.commit()
        else:
            break
    # 关闭
    out.close
    cur.close()
    conn.close()



insert_data("course",'D:\zixun\course\course.csv')