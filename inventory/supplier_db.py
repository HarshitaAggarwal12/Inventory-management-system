import sqlite3
def supplier_db():
    con = sqlite3.connect(database='supplier.db')
    cur=con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS supply(sup_id text,InvoiceNo text,Name text,Contact text,Description text)")
    con.commit()



supplier_db()