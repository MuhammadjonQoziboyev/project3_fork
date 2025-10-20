import sqlite3
from datetime import date, timedelta
import random

# Bazani ochamiz
conn = sqlite3.connect("bookstore.db")
ish = conn.cursor()

# Jadvallarni yaratish (agar yo'q bo'lsa)
ish.execute("""
CREATE TABLE IF NOT EXISTS muallif (
    id INTEGER PRIMARY KEY,
    name TEXT,
    yili DATE
)
""")

ish.execute("""
CREATE TABLE IF NOT EXISTS kitob (
    id INTEGER PRIMARY KEY,
    name TEXT,
    yili INTEGER,
    nashriyot TEXT,
    muallifId INTEGER NOT NULL,
    FOREIGN KEY (muallifId) REFERENCES muallif(id) ON DELETE CASCADE
)
""")

ish.execute("""
CREATE TABLE IF NOT EXISTS sklad (
    id INTEGER PRIMARY KEY,
    kitobId INTEGER,
    soni INTEGER,
    summasi INTEGER,
    FOREIGN KEY (kitobId) REFERENCES kitob(id) ON DELETE SET NULL
)
""")

ish.execute("""
CREATE TABLE IF NOT EXISTS soldBook (
    id INTEGER PRIMARY KEY,
    kitobId INTEGER,
    soni INTEGER,
    soldSummasi INTEGER,
    sana DATE,
    FOREIGN KEY (kitobId) REFERENCES kitob(id) ON DELETE SET NULL
)
""")

# -------------------------------------------
# 1. muallif - 20 ta
mualliflar = []
for i in range(1, 21):
    name = f"Muallif_{i}"
    yili = f"{random.randint(1870, 1990)}-01-01"
    mualliflar.append((i, name, yili))

ish.executemany("INSERT INTO muallif (id, name, yili) VALUES (?, ?, ?)", mualliflar)

# -------------------------------------------
# 2. kitob - 20 ta
kitoblar = []
for i in range(1, 21):
    name = f"Kitob_{i}"
    yili = random.randint(1950, 2023)
    nashriyot = f"Nashriyot_{random.randint(1,5)}"
    muallifId = random.randint(1, 20)
    kitoblar.append((i, name, yili, nashriyot, muallifId))

ish.executemany("INSERT INTO kitob (id, name, yili, nashriyot, muallifId) VALUES (?, ?, ?, ?, ?)", kitoblar)

# -------------------------------------------
# 3. sklad - 20 ta
skladlar = []
for i in range(1, 21):
    kitobId = i  # har bir kitob uchun bitta sklad
    soni = random.randint(10, 100)
    summasi = soni * random.randint(10000, 50000)
    skladlar.append((i, kitobId, soni, summasi))

ish.executemany("INSERT INTO sklad (id, kitobId, soni, summasi) VALUES (?, ?, ?, ?)", skladlar)

# -------------------------------------------
# 4. soldBook - 20 ta
sold_books = []
# bu joyda sikl orqali sanani random qilinmoqda
for i in range(1, 21):
    kitobId = random.randint(1, 20)
    soni = random.randint(1, 10)
    soldSummasi = soni * random.randint(
        12000, 60000)
    sana = date(2025, 9, 1) + timedelta(days=random.randint(0, 21))
    sold_books.append((i, kitobId, soni, soldSummasi, sana))

ish.executemany("INSERT INTO soldBook (id, kitobId, soni, soldSummasi, sana) VALUES (?, ?, ?, ?, ?)", sold_books)

# -------------------------------------------
# Saqlash va yopish
# bu joyda o`zgarishlar bazaga yuborilmoqda va baza yoplidi
conn.commit()
conn.close()

print("✅ Har bir jadvalga 20 tadan ma'lumot muvaffaqiyatli kiritildi.")
