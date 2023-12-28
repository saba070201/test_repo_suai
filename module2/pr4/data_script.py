import sqlite3
import names 
import random 

def initial_tables(conn: sqlite3.connect, cur):
    """
    Создать таблицу в базе данных  
    """
    cur.execute("""
    CREATE TABLE IF NOT EXISTS staff  (
        id  INTEGER PRIMARY KEY AUTOINCREMENT ,
        name TEXT NOT NULL,
        salary INTEGER ,
        position TEXT ,
        qualification TEXT
    )
    """)
    conn.commit()
def set_data_to_db(conn,cur,qualifications,positions):
    """
    Заполнить таблицу в базе данных 
    """
    for i in range(10000):
        qualification=random.choice(list(qualifications.keys()))
        position=random.choice(positions)
        salary=random.choice(qualifications[qualification])
        cur.execute("""INSERT INTO staff(name,salary,position,qualification) VALUES(?,?,?,?);""",(names.get_full_name(),salary,position,qualification))

        conn.commit()

def get_data_from_db(conn,cur):
    """
    Получить данные из базы данных
    """
    data=cur.execute(""" SELECT * FROM staff;""")
    return data.fetchall()

data_sample_qualification = {'Junior': [300,1000],'Middle':[900,5000],'Senior':[3000,10000],'God':[10000,9999999]}
data_sample_positions=['Backend developer','Frontend developer','Project manager']
DB_PATH='testdb.db'
conn = sqlite3.connect(DB_PATH)
cur=conn.cursor()
# initial_tables(conn=conn,cur=cur)
# set_data_to_db(conn=conn,cur=cur,qualifications=data_sample_qualification,positions=data_sample_positions)
# print(get_data_from_db(conn=conn,curr=cur))
conn.close()

