import sqlite3

dbname = 'fast.db'

def name(dbname):
    conn = sqlite3.connect(dbname)
    # conn.row_factory = sqlite3.Row
    cur = conn.cursor()
# terminalで実行したSQL文と同じようにexecute()に書く
    cur.execute('SELECT name FROM users')

# 中身を全て取得するfetchall()を使って、printする。
    data = cur.fetchall()
    users_list = []
    for i in data:
        users_list.append(i)
    
        
    cur.close()
    conn.close()
    return users_list

def password(dbname):
    conn = sqlite3.connect(dbname)
    # conn.row_factory = sqlite3.Row
    cur = conn.cursor()
# terminalで実行したSQL文と同じようにexecute()に書く
    cur.execute('SELECT password FROM users')

# 中身を全て取得するfetchall()を使って、printする。
    data = cur.fetchall()
    users_list = []
    for i in data:
        users_list.append(i)
    
        
    cur.close()
    conn.close()
    return users_list

def dict_user(dbname, name):
    num = 0
    conn = sqlite3.connect(dbname)
    # conn.row_factory = sqlite3.Row
    cur = conn.cursor()
# terminalで実行したSQL文と同じようにexecute()に書く
    cur.execute('SELECT * FROM users')
    

# 中身を全て取得するfetchall()を使って、printする。
    data = cur.fetchall()
    users_list = []
    for i in data:
        # print(i[0])
        # print(name)
        if i[0] == name:
            users_list.append(i)
            # print(i)
            break;
        # num += 1
        # users_list.append(i)
        
    cur.close()
    conn.close()
    return users_list

# name = "kuso"
# s = dict_user(dbname, name)
# print(s[0][1])