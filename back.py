import sqlite3

db = sqlite3.connect('tododb')
c = db.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS todo(Task TEXT,Priority INTEGER)''')
c.execute('''CREATE TABLE IF NOT EXISTS done(Task TEXT)''')
db.commit()


def write(task, priority=1):
    c.execute('''INSERT into todo (Task, Priority) VALUES(?,?) ''', (task, priority))
    db.commit()


def readtask():
    c = db.cursor()
    c.execute('''select Task from todo order by Priority''')
    data = c.fetchall()
    db.commit()
    return data


def readpriority():
    c = db.cursor()
    c.execute('''select Priority from todo order by Priority''')
    data = c.fetchall()
    db.commit()
    return data


def cleartable():
    c.execute('''delete from todo''')
    db.commit()


def delete(x):
    c.execute('''delete from todo where Task=?''', x)
    db.commit()


def readcompleted():
    c = db.cursor()
    c.execute('''select Task from done order by Task''')
    data = c.fetchall()
    db.commit()
    return data


def deletecompleted(x):
    c.execute('''delete from done where Task=?''', x)
    db.commit()

def deleteallcompleted():
    c.execute('''delete from done''')
    db.commit()

def complete(x):
    c.execute('''INSERT into done (Task) VALUES(?) ''', (x))
    c.execute('''delete from todo where Task=? ''', (x))
    db.commit()

