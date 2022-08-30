import pymysql as p
def connect():
    con=p.connect(user="root", password="", host="localhost", database="bankdata")
    cur=con.cursor()
    return con,cur

def insert_data(t):
    con,cur=connect()
    q="insert into bank (acc_no,name, balance) values (%s,%s,%s) "
    cur.execute(q, t)
    con.commit()
    con.close()
def access_accno():
    con,cur=connect()
    q="select acc_no from bank "
    cur.execute(q)
    data=cur.fetchall()
    l=[]
    for i in data:
        l.append(i[0])
    con.commit()
    con.close()
    return l

def access_balance(mid) :
    con,cur=connect()
    q="select balance from bank where id=%s"
    cur.execute(q,mid)
    data=cur.fetchall()
    con.commit()
    con.close()
    return data [0][0]

def add_balance(tu):
    con,cur=connect()
    q="update bank set balance=%s where id=%s;"
    cur.execute(q,tu)
    con.commit()
    con.close()
    
def wd_balance(t):
    con,cur=connect()
    q="update bank set balance=%s where id=%s"
    cur.execute(q,t)
    con.commit()
    con.close()
    
def update_data(t):
    con,cur=connect()
    q="update bank set acc_no=%s,name=%s where id=%s;"
    cur.execute(q,t)
    con.commit()
    con.close()
    
def display_data():
    con,cur=connect()
    q="select * from bank;"
    cur.execute(q)
    data=cur.fetchall()
    for i in data:
        print("id no   : ",i[0])
        print("acc no  : ",i[1])
        print("name    : ",i[2])
        print("balance : ",i[3])
        print("----------------------------------------------------------------------")
    con.commit()
    con.close()

def delete_data(myid):
    con,cur=connect()
    q="delete from bank where id=%s"
    cur.execute(q,myid)
    con.commit()
    con.close()

    
while True:
    ch=int(input("press 1 : create new account\npress 2 : update balance\npress 3 : update acc no or name\npress 4 : display details\npress 5 : delete account\npress 6 : exit\n"))
    if ch==1:
        a=int(input("enter account number\n"))
        allno=access_accno()
        while a in allno:
            print("account no already exists, please enter new no.")
            a=int(input("enter account number\n"))
        
        n=input("enter your name\n")
        b=int(input("enter your balance\n"))
        t= (a,n,b)
        insert_data(t)
    elif ch==2:
        mid=int(input("enter id number \n"))
        rev=access_balance(mid)
        z=int(input("press 1 :deposit\npress 2 :withdraw\n"))
        if z==1:
            am=int(input("enter amount\n"))
            dep=rev+am
            tu=(dep,mid)
            add_balance(tu)
        elif z==2:
            am=int(input("enter amount\n"))
            if rev>=am:
                wd=rev-am
                t=(wd,mid)
                wd_balance(t)
            else:
                print("insufficient balance please enter valid amount")
            
        else:
            print("enter valid number")
    elif ch==3:
        mid=int(input("enter id number \n"))
        a=int(input("enter account number\n"))
        n=input("enter your name\n")
        t=(a,n,mid)
        update_data(t)
    elif ch==4:
        display_data()
        
    elif ch==5:
        myid=int(input("enter id number\n"))
        delete_data(myid)
    elif ch==6:
        break

        
        
        
        
            
