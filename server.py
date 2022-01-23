import socket
from threading import Thread
import mysql.connector

conns = socket.socket()
conns.bind(('127.0.0.1',12345))
conns.listen(5)
print("======================================================= Server Exectution Started =================================================")

def fun(c,addr):
    query=c.recv(1024).decode()
    mydb = mysql.connector.connect(host="localhost",user="root",password="",database="poemds")
    mycursor=mydb.cursor()
    mycursor.execute(query)
    c.send(", ".join(map(str, mycursor.fetchall())).encode())
    c.close()

while True:
    c, addr = conns.accept()
    thread = Thread(target = fun , args=(c,addr) )
    thread.start()