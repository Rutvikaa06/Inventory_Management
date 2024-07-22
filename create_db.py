import sqlite3
def create_db():
    con=sqlite3.connect(database=r'ims.db')
    cur=con.cursor()

    cur.execute("CREATE TABLE IF NOT EXISTS supplier(invoice INTEGER PRIMARY KEY AUTOINCREMENT,name text,contact text,desc text)")
    con.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS category(cid INTEGER PRIMARY KEY AUTOINCREMENT,name text)")
    con.commit()
    
    cur.execute("CREATE TABLE IF NOT EXISTS product(pid INTEGER PRIMARY KEY AUTOINCREMENT,Supplier text,Category text,name text,price text,qty text,status text)")
    con.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS register(id INTEGER PRIMARY KEY AUTOINCREMENT,f_name text,l_name text,contact text,email text,utype text,question text,answer text,password text)")
    con.commit()

create_db()