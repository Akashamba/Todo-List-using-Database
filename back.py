import sqlite3


db = sqlite3.connect('tododb')
c = db.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS todo(ItemNo INTEGER ,Task TEXT,Priority INTEGER)''')
db.commit()


def write(task, priority):
    c.execute('''INSERT into todo(Task, Priority) VALUES(?,?)''',(task, priority))
    db.commit()


def readall():
    c=db.cursor()
    c.execute('''select * from todo order by Priority''')
    data=c.fetchall()
    db.commit()
    return data



