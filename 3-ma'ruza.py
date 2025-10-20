import sqlite3

from kiritish import cursor

con=sqlite3.connect("bookstore.db")
cur=con.cursor()
jadval=cur.execute("select MAX(sk.summasi) from kitob k join sklad sk  on k.id=sk.kitobId ")

for talaba in jadval.fetchall():
   print("eng qimmat kitob==",talaba)
jadval1=cur.execute("select MIN(sk.summasi) from kitob k join sklad sk  on k.id=sk.kitobId ")
print("eng arzon kitob",jadval1.fetchone())
soni=cur.execute("select sum(sk.soni) from kitob k join sklad sk  on k.id=sk.kitobId ")
print("jami kitoblar soni=", soni.fetchone())
summa=cur.execute("select sum(sk.soni*sk.summasi) from kitob k join sklad sk  on k.id=sk.kitobId ")
print("umumiy ", summa.fetchone()," sum miqdorda mahsulot bor")
