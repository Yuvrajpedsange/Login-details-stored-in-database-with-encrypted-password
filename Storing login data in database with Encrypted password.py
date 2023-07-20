#These are the modules
import tkinter
import mysql.connector
from cryptography.fernet import Fernet

#This is to connect mysql
#Here, I used my localhost name and password
con=mysql.connector.connect(host="localhost",user='root',password="1234")
cur=con.cursor(buffered=True)


#This is for database
try:
    cur.execute("use registration")
except:
    cur.execute("create database registration")
    cur.execute("use registration")


#This is for table inside database
try:
    cur.execute("describe persons")
except:
    cur.execute("create table persons(id int primary key auto_increment,name varchar(30),age int,gender varchar(10),email varchar(30),Mobile varchar(10),password varchar(100))")


#Key for encryption
fernet_key = b'k5Gh5UDt7VzwZikHaC07jXqCQjo0BXMvXeALtb_Uiws='
f_obj = Fernet(fernet_key)  #fernet is used for to read only data we can't change once created


#Encrypt the password by using Fernet object of cryptography module
def encrypt_password(password):
    return f_obj.encrypt(password.encode())

def Registration():
    #Password is encrypted before insertion to the database
    encrypted_password = encrypt_password(e6.get())

    #Insert the encrypted password and other details in database
    cur.execute(f"insert into persons(name,age,gender,email,mobile,password) "
                f"value ('{e1.get()}','{e2.get()}','{e3.get()}','{e4.get()}','{e5.get()}','{encrypted_password.decode()}')")
    con.commit()


#This will close the tkinter window
def destroy():
    win.destroy()

win=tkinter.Tk()
win.geometry("300x250")

#This is Title of Page
win.title("---- Person Registration details ----")

#Thses are the labels
l1=tkinter.Label(win, text="Personnel Details")
l2=tkinter.Label(win, text="Name = ")
l3=tkinter.Label(win, text="Age = ")
l4=tkinter.Label(win, text="Gender = ")
l5=tkinter.Label(win, text="Email = ")
l6=tkinter.Label(win, text="Phone Number = ")
l7=tkinter.Label(win, text="Password = ")

l1.grid(row=1,column=1)
l2.grid(row=2,column=1)
l3.grid(row=3,column=1)
l4.grid(row=4,column=1)
l5.grid(row=5,column=1)
l6.grid(row=6,column=1)
l7.grid(row=7,column=1)


#Variables for the storage of data
Namevalue =tkinter.StringVar()
Agevalue =tkinter.IntVar()
Gendervalue =tkinter.StringVar()
Emailvalue =tkinter.StringVar()
Phone_Number_value =tkinter.IntVar()
Passwordvalue =tkinter.StringVar()

#This will take input for above labels
e1=tkinter.Entry(win, textvariable=Namevalue)
e2=tkinter.Entry(win, textvariable=Agevalue)
e3=tkinter.Entry(win, textvariable=Gendervalue)
e4=tkinter.Entry(win, textvariable=Emailvalue)
e5=tkinter.Entry(win, textvariable=Phone_Number_value)
e6=tkinter.Entry(win, textvariable=Passwordvalue)

e1.grid(row=2,column=2)
e2.grid(row=3,column=2)
e3.grid(row=4,column=2)
e4.grid(row=5,column=2)
e5.grid(row=6,column=2)
e6.grid(row=7,column=2)

#This is for the submit button
b=tkinter.Button(win, text="Submit Here",command=lambda:[Registration(),destroy()])
b.grid(row=8,column=1)

win.mainloop()