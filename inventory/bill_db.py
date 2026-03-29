import sqlite3

def bill_db():
    con = sqlite3.connect(database='bill.db')
    cur=con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS bill(Product_id text,Customer_Name text,Product_Name TEXT,Contact text,Price_per_qty text, Quantity text)")

    con.commit()



bill_db()