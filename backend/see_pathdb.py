import sqlite3
import json

dbname = 'fast.db'
name = "12_3_4_5_7"
num = 5

def photo_list(name:str, num : int):
    photolist = [] 
    j = ""
    for x in name:
        if x == "_":
            photolist.append(j)
            # print(j)
            j = ""
        else:
            j += x
    if len(photolist) != num:
        if name[-2] == "_":
            photolist.append(name[-1])
            # print(name[-1])
        else:
            photolist.append(name[-2:]) 
            # print(name[-2:]) 
    return photo_list
            
              

def user_photo(name:list):
    dbname = 'fast.db'
    conn = sqlite3.connect(dbname)
    # conn.row_factory = sqlite3.Row
    cur = conn.cursor()
# terminalで実行したSQL文と同じようにexecute()に書く
    cur.execute('SELECT path FROM path')

# 中身を全て取得するfetchall()を使って、printする。
    data = cur.fetchall()
    
    users_list = []
    for i in name:
        users_list.append(data[i])  
    cur.close()
    conn.close()
    return users_list


# name = "kuso"
# name = photo_list(name, num)
# print(user_photo(name))

# for i in s:
# print(xbox)