import sqlite3
connect=sqlite3.connect("baza2.db")
ish=connect.cursor()

ish.execute(" create table if not exists muallif ( id integer primary key, name string, yili Date)")
ish.execute(" create table if not exists kitob ( id integer primary key, name string, yili Integer, nashriyot string, muallifId integer not null, foreign key (muallifId) references muallif(id) on delete cascade)")
ish.execute(" create table if not exists sklad ( id integer primary key,  kitobId integer, soni integer, summasi integer, foreign key (kitobId) references kitob(id) on delete set null)")

ish.execute(" create table if not exists soldBook ( id integer primary key,  kitobId integer, soni integer, soldSummasi integer, sana Date, foreign key (kitobId) references kitob(id) on delete set null)")
connect.commit()
ish.close()
connect.close()