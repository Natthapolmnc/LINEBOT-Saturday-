import sqlite3

def importfood():
    tuple1=()
    with sqlite3.connect('test2.sqlite') as db:
        sql_cmd = 'select * from TABLE1'
        for row in db.execute(sql_cmd):
            tuple1+=row
    return tuple1
