import sqlite3

def category_db():
    con = sqlite3.connect(database='category.db')
    cur=con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS category(Category_id INTEGER PRIMARY KEY AUTOINCREMENT,Name TEXT NOT NULL)")

    con.commit()



category_db()




