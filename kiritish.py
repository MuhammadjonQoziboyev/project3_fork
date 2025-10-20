import sqlite3

conn = sqlite3.connect("school.db")
cursor = conn.cursor()
cursor.execute("PRAGMA foreign_keys = ON")

cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
)
""")
cursor.execute("""
CREATE TABLE IF NOT EXISTS subjects (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE
)
""")

# Baholar jadvali
cursor.execute("""
CREATE TABLE IF NOT EXISTS grades (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER,
    subject_id INTEGER,
    grade INTEGER,
    FOREIGN KEY(student_id) REFERENCES students(id),
    FOREIGN KEY(subject_id) REFERENCES subjects(id)
)
""")
conn.commit()

subjects = [("Matematika",), ("Fizika",), ("Ingliz tili",)]
cursor.executemany("INSERT OR IGNORE INTO subjects (name) VALUES (?)", subjects)
conn.commit()

cursor.execute("INSERT INTO students (name) VALUES (?)", ("Vali",))
student_id = cursor.lastrowid

# Fanning ID sini olish uchun yordamchi funksiya
def get_subject_id(subject_name):
    cursor.execute("SELECT id FROM subjects WHERE name = ?", (subject_name,))
    result = cursor.fetchone()
    return result[0] if result else None

# Baholar ro'yxati: (fan_nomi, baho)
input_grades = [
    ("Matematika", 5),
    ("Fizika", 4),
    ("Ingliz tili", 5)
]

# subject_id'larni olish
grades_to_insert = []
for subject_name, grade in input_grades:
    subject_id = get_subject_id(subject_name)
    if subject_id:
        grades_to_insert.append((student_id, subject_id, grade))

# Baholarni qo‘shish
cursor.executemany(
    "INSERT INTO grades (student_id, subject_id, grade) VALUES (?, ?, ?)",
    grades_to_insert
)

conn.commit()

