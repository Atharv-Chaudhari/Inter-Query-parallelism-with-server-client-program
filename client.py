import socket
c=socket.socket()
connect_me=0
try:
    c.connect(('127.0.0.1',12345))
    connect_me=1
except:
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Error No Active Server Found ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
if(connect_me==1):
    print("======================================================= Client Exectution Started ================================================")
    query = input("Query :-\n")
    c.send((query.encode()))
    if "select" in query.lower():
        print("======================================================= Result of Query ======================================================")
        rcv=c.recv(1028).decode()
        cn=rcv.count('(')
        flag=0
        for i in range(cn):
            print(rcv[:rcv.index(')')]+")")
            rcv=rcv[rcv.index(')')+1:]
            if(flag!=cn-1):
                rcv=rcv[rcv.index(',')+2:]
            flag=flag+1
        print("=================================================================================================================================")
    else:
        print("Results Of Query Execution :- \n",c.recv(1028).decode())