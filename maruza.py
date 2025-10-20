import sqlite3
from datetime import datetime

connect=sqlite3.connect("baza2.db")
ish=connect.cursor()
ism=input('Muallif FIO ni kiriting')
yili=input(' tugilgan sanasini kiritish (dd/mm/yyyy)')
#ish.execute(" insert into muallif(name, yili) values ('Abdulla Qodiriy', 10/04/1894)")
#ish.execute(" insert into muallif(name, yili) values ('Alisher Navoiy', '09/02/1441')")
#ish.execute("delete from muallif where id<6 ")
#ish.execute("update muallif set yili='09/02/1441' where yili=-1434")
ish.execute(f" insert into muallif(name, yili) values('{ism}', '{yili}') ")


author=ish.execute("select * from muallif")

#author.fetchall()
for i in author.fetchall():
    print(i)
ish.close()
connect.commit()
connect.close()