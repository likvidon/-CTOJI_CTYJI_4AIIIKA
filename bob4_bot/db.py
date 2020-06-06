import os
import sqlite3


conn = sqlite3.connect(os.path.join('myDB.db'))
c = conn.cursor()

def add_new_user(user_id, selfie_path):
    c.execute("INSERT INTO users (user_id, user_selfie_path) VALUES (" + str(user_id) ", " + selfie_path + ")")
    