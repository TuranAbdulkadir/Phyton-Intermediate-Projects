import sqlite3

conn = sqlite3.connect('data.db')
c = conn.cursor()
c.execute('CREATE TABLE IF NOT EXISTS expenses (name TEXT, price REAL)')

def add():
    n = input("Item: ")
    p = float(input("Price: "))
    c.execute('INSERT INTO expenses VALUES (?,?)', (n,p))
    conn.commit()

def show():
    for row in c.execute('SELECT * FROM expenses'): print(row)

while True:
    opt = input("1-Add, 2-Show, 3-Exit: ")
    if opt=='1': add()
    elif opt=='2': show()
    elif opt=='3': break