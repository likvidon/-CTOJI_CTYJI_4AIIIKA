import os
import sqlite3


conn = sqlite3.connect(os.path.join('myDB.db'))
c = conn.cursor()

def createUser(user_id, result):
    if(findResult(user_id)):
        c.execute("DELETE FROM users WHERE user_id=" + "'" + str(user_id) + "'")
    c.execute("INSERT INTO users (user_id, result) VALUES (" + str(user_id) + ", " + result + ")")
    conn.commit()
    print('user created')

def findResult(user_id):
    c.execute("SELECT * from users WHERE user_id='" + str(user_id) + "'")
    res = c.fetchone()
    if (res):
        return res[2]
    else:
        return res
