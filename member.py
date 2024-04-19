# coding=utf-8
import sqlite3
import sys
import re
from model import Model
class Member(Model):
    def __init__(self):
        self.con=sqlite3.connect(self.mydb)
        self.con.row_factory = sqlite3.Row
        self.cur=self.con.cursor()
        self.cur.execute("""create table if not exists member(
        id integer primary key autoincrement,
        name text,
            band_id text
                    );""")
        self.con.commit()
        #self.con.close()
    def getallbybandid(self,bandid):
        self.cur.execute("select * from member where band_id = ?",(bandid,))

        row=self.cur.fetchall()
        return row
    def getall(self):
        self.cur.execute("select * from member")

        row=self.cur.fetchall()
        return row
    def deletebyid(self,myid):

        self.cur.execute("delete from member where id = ?",(myid,))
        job=self.cur.fetchall()
        self.con.commit()
        return None
    def getbyid(self,myid):
        self.cur.execute("select * from member where id = ?",(myid,))
        row=dict(self.cur.fetchone())
        print(row["id"], "row id")
        job=self.cur.fetchall()
        return row
    def create(self,params):
        print("ok")
        myhash={}
        for x in params:
            if 'confirmation' in x:
                continue
            if 'envoyer' in x:
                continue
            if '[' not in x and x not in ['routeparams']:
                #print("my params",x,params[x])
                try:
                  myhash[x]=str(params[x].decode())
                except:
                  myhash[x]=str(params[x])
        print("M Y H A S H")
        print(myhash,myhash.keys())
        myid=None
        try:
          self.cur.execute("insert into member (name,band_id) values (:name,:band_id)",myhash)
          self.con.commit()
          myid=str(self.cur.lastrowid)
        except Exception as e:
          print("my error"+str(e))
        azerty={}
        azerty["member_id"]=myid
        azerty["notice"]="votre member a été ajouté"
        return azerty




