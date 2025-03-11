import pymysql
from tkinter import messagebox
def connect_database():
    global mycursor
    global conn

    try:
        conn=pymysql.connect(host="localhost",user="root",password='csfera04')
        mycursor=conn.cursor()
    except:
        messagebox.showerror(title="Error",message="please try again")
        return
    mycursor.execute("CREATE DATABASE IF NOT EXISTS employee_data")
    mycursor.execute("USE employee_data")
    mycursor.execute("""
            CREATE TABLE IF NOT EXISTS data (
                Id VARCHAR(30),
                Name VARCHAR(100),
                Phone VARCHAR(15),
                Role VARCHAR(50),
                Gender VARCHAR(20),
                Salary DECIMAL(10,2)
                
            )
        """)
def insert(id,name,phone,role,gender,salary):
    mycursor.execute("INSERT INTO data values(%s,%s,%s,%s,%s,%s)",(name,phone,role,gender,salary,id))
    conn.commit()
def id_exists(id):
    mycursor.execute("SELECT COUNT(*) FROM data WHERE Id = %s",id)
    result=mycursor.fetchone()
    return result[0]>0
def fetch_employees():
    mycursor.execute('SELECT * from data')
    result=mycursor.fetchall()
    return result
def update(id,name,phone,role,gender,salary):
    mycursor.execute('UPDATE data SET name=%s,phone=%s,role=%s,gender=%s,salary=%s Where id=%s',(id,name,phone,role,gender,salary))
    conn.commit()

connect_database()
