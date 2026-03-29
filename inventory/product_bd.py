import sqlite3

def product_db():
    con = sqlite3.connect(database='product.db')
    cur=con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS product(Product_id INTEGER PRIMARY KEY AUTOINCREMENT,Category text, Supplier text, Name text, Price text, Quantity text, Status text)")

    con.commit()



product_db()