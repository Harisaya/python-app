import sqlite3

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

def connect_db():
    conn = sqlite3.connect('data/database.db')
    conn.row_factory = dict_factory
    return conn

def insert_user(name, email, password, gender="Không tiết lộ", avatar=""):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO users (name, email, password, gender, avatar)
        VALUES (?, ?, ?, ?, ?)
    ''', (name, email, password, gender, avatar))
    conn.commit()
    conn.close()

def get_user_by_id(user_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT id, name, email, password, gender, avatar, birthday, age FROM users WHERE id = ?', (user_id,))
    user = cursor.fetchone()
    conn.close()
    return user

def get_user_by_email(email):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT id, name, email, password, gender, avatar, birthday, age FROM users WHERE email = ?', (email,))
    user = cursor.fetchone()
    conn.close()
    return user

def get_user_by_name(name):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT id, name, email, password, gender, avatar, birthday, age FROM users WHERE name = ?', (name,))
    user = cursor.fetchone()
    conn.close()
    return user

def get_user_by_email_and_password(email, password):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT id, name, email, password, gender, avatar, birthday, age FROM users WHERE email = ? AND password = ?', (email, password))
    user = cursor.fetchone()
    conn.close()
    return user

def update_avatar_user(user_id, avatar):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('UPDATE users SET avatar = ? WHERE id = ?', (avatar, user_id))
    conn.commit()
    conn.close()

def update_user(user_id, name, email, gender, birthday, age):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET name = ?, email = ?, gender = ?, birthday = ?, age = ? WHERE id = ?", (name, email, gender, birthday, age, user_id))
    conn.commit()
    conn.close()

def remove_user(user_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM users WHERE id = ?', (user_id,))
    conn.commit()
    conn.close()
