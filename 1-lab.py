import sqlite3

conn=sqlite3.connect('baza.db')
a=conn.cursor()
a.execute(" create table if not exists muallif ( id  integer primary Key, name string, "
          "janri string, yili date )")

a.execute(" create table if not exists kitob ( id  integer primary Key, name string, "
          "yili Date, nashriyoti String, muallifId Integer not null, Foreign key(muallifId) "
          "references muallif(id)  on delete   cascade)")
a.execute(" create table if not exists sklad ( id  integer primary Key, "
          "kitobId Integer not null, soni Integer, summasi Integer, "
          "Foreign key(kitobId) references kitob(id)  on delete   cascade)")

a.execute(" create table if not exists sold ( id  integer primary Key, "
          "kitobId Integer not null, soni Integer, summasi Integer, sana Date,  "
          "Foreign key(kitobId) references kitob(id)  on delete   cascade)")


conn.commit()
a.close()
conn.close()

