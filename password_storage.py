from tkinter import *
from datetime import datetime
import _sqlite3
from tkinter import messagebox
from random import randint

root=Tk()
root.title("Cybertron Shadow")
root.geometry("600x600")

number=randint(1234567890,9876543210)
date=datetime.now()
tim=date.strftime('%B %d, %Y     {}:{:02d}'.format(date.hour,date.minute))

title_label=Label(root,text="CYBERTRON SHADOW",fg="yellow",font=("arial",40,"italic"),justify=CENTER)
title_label.grid(row=0,column=0,columnspan=2)

#Creating the database

connection=_sqlite3.connect("password~storage.db")
curso=connection.cursor()
'''
#creating the table
curso.execute("""CREATE TABLE password(
                random integer,
                website text,
                username text,
                password text
                )""")
'''
connection.commit()

connection.close()


def exit():
    quiz=messagebox.askyesno("cybertron shadow","Do you want to exit")
    if quiz == 1:
        root.destroy()

def save ():
    passw = "I am Cybertron Shadow"
    passw2 = mmpassword.get()
    if username_entry.get() != "" and password_entry.get() != "" and website_entry.get() != "" and passw == passw2:
        connection = _sqlite3.connect("password~storage.db")
        curso = connection.cursor()
        curso.execute("INSERT INTO password VALUES (:random, :website, :username, :password)",
                      {
                          'random':random_entry.get(),
                          'website':website_entry.get(),
                          'username':username_entry.get(),
                          'password':password_entry.get()
                      })

        connection.commit()

        connection.close()

        random_entry.delete(0, END)
        username_entry.delete(0, END)
        website_entry.delete(0, END)
        password_entry.delete(0, END)
        mmpassword.delete(0,END)

        messagebox.showinfo("cybertron shadow","INFORMATION SAVED")
    else:
        messagebox.showinfo("cybertron shadow", "CHECK YOUR ENTRY")

def dview():
    passw="I am Cybertron Shadow"
    passw2=mmpassword.get()
    if passw==passw2:
        mmpassword.delete(0, END)
        connection = _sqlite3.connect("password~storage.db")
        curso = connection.cursor()

        curso.execute("SELECT *, oid FROM password")
        records=curso.fetchall()

        disrecords=''
        for record in records:
            disrecords += str(record[1]) + "  " + "\t" + str(record[2]) + "  "  + "\t" + str(record[3]) + "    " +str(record[4]) + '\n'

        window=Toplevel()
        window.title("shadow system")
        window.geometry("400x400")
        label1=Label(window,text="website       username     password      oid",fg="green",font=("ariana",10,"italic"))
        label1.grid(row=0,column=0,columnspan=2)

        label=Label(window,text=disrecords,justify=LEFT)
        label.grid(row=1,column=0,columnspan=2)

        connection.commit()

        connection.close()
    elif passw2 == "":
        messagebox.showinfo("cybertron shadow","input password")

    else :
        messagebox.showinfo("cybertron shadow","Wrong password")

def delete ():
    oid=selectoid.get()
    passw = "I am Cybertron Shadow"
    passw2 = mmpassword.get()
    try:
        if oid > str(0) and passw == passw2:
            mmpassword.delete(0, END)
            connection = _sqlite3.connect("password~storage.db")
            curso = connection.cursor()

            curso.execute("DELETE from password WHERE oid=" + selectoid.get())

            connection.commit()

            connection.close()
            messagebox.showinfo("cybertron shadow","iformation deleted")
        else:
            messagebox.showinfo("cybertron shadow","incorrect information")
    except IOError:
        messagebox.showinfo("shadow system", "no oid selected")

def edit ():
    passw = "I am Cybertron Shadow"
    passw2 = mmpassword.get()
    if passw == passw2 :
        mmpassword.delete(0,END)
        window1 = Toplevel()
        window1.title("shadow system")
        window1.geometry("400x400")
        def ssave():
            connection = _sqlite3.connect("password~storage.db")
            curso = connection.cursor()
            roid=selectoid.get()
            curso.execute("""UPDATE password SET
            website= :web,
            username= :name,
            password= :pass
            
            WHERE oid= :oid""",
                          {
                              'web':website_entry1.get(),
                              'name':username_entry1.get(),
                              'pass':password_entry1.get(),
                              'oid':roid
                          }
            )

            connection.commit()

            connection.close()
            username_entry1.delete(0, END)
            website_entry1.delete(0, END)
            password_entry1.delete(0, END)

            messagebox.showinfo("cybertron shadow", "UPDATE SUCCESFUL")

        website_label1 = Label(window1, text="Website", fg="yellow", font=("arial", 20, "bold"))
        website_label1.grid(row=1, column=0, padx=10, pady=10)
        website_entry1 = Entry(window1, bg="blue", width=30, bd=4, borderwidth=5)
        website_entry1.grid(row=1, column=1)

        username_label1 = Label(window1, text="Username", fg="yellow", font=("arial", 20, "bold"))
        username_label1.grid(row=2, column=0)
        username_entry1 = Entry(window1, bg="blue", width=30, bd=4, borderwidth=5)
        username_entry1.grid(row=2, column=1, padx=10, pady=10)

        password_label1 = Label(window1, text="Password", fg="yellow", font=("arial", 20, "bold"))
        password_label1.grid(row=3, column=0)
        password_entry1 = Entry(window1, bg="blue", width=30, bd=4, borderwidth=5)
        password_entry1.grid(row=3, column=1, padx=10, pady=10)

        #save button
        save_button = Button(window1,text="save", fg="black", bg="green", font=("arial", 10, "bold"), width=10, padx=16, pady=14 ,bd=7, justify=CENTER,command=ssave)
        save_button.grid(row=4, column=0)

        connection = _sqlite3.connect("password~storage.db")
        curso = connection.cursor()
        id=selectoid.get()
        curso.execute("SELECT * FROM password WHERE oid=" + id)
        records = curso.fetchall()

        for record in records:
            website_entry1.insert(0,record[1])
            username_entry1.insert(0,record[2])
            password_entry1.insert(0,record[3])
    else :
        messagebox.showinfo("shadow tech","enter password and oid to edit")

random_label=Label(root,text="Random",fg="yellow",font=("arial",20,"bold"))
random_label.grid(row=1,column=0,padx=10,pady=10)
random_entry=Entry(root,bg="blue",width=30,bd=4, borderwidth=5)
random_entry.grid(row=1,column=1)
random_entry.insert(0,number)

website_label=Label(root,text="Website",fg="yellow",font=("arial",20,"bold"))
website_label.grid(row=2,column=0,padx=10,pady=10)
website_entry=Entry(root,bg="blue",width=30,bd=4, borderwidth=5)
website_entry.grid(row=2,column=1)

username_label=Label(root,text="Username",fg="yellow",font=("arial",20,"bold"))
username_label.grid(row=3,column=0)
username_entry=Entry(root,bg="blue",width=30,bd=4, borderwidth=5)
username_entry.grid(row=3,column=1,padx=10,pady=10)

password_label=Label(root,text="Password",fg="yellow",font=("arial",20,"bold"))
password_label.grid(row=4,column=0)
password_entry=Entry(root,bg="blue",width=30,bd=4, borderwidth=5)
password_entry.grid(row=4,column=1,padx=10,pady=10)

oidlabel=Label(root,text="SELECT OID",fg="yellow",font=("arial",20,"bold"))
oidlabel.grid(row=8,column=0)
selectoid=Entry(root,bg="blue",width=30,bd=4, borderwidth=5)
selectoid.grid(row=8,column=1)

mpassword = Label(root, text="enter password", fg="yellow", font=("arial", 20, "bold"))
mpassword.grid(row=9, column=0)
mmpassword= Entry(root, bg="blue", width=30, bd=4, borderwidth=5)
mmpassword.grid(row=9, column=1)

#Creating buttons
save_button=Button(text="save",fg="black",bg="green",font=("arial",10,"bold"),width=10, padx=16, pady=14,bd=7,justify=RIGHT,command=save)
save_button.grid(row=5,column=0)
delete_button=Button(text="delete",fg="black",bg="green",font=("arial",10,"bold"),width=10, padx=16, pady=14,bd=7,justify=LEFT,command=delete)
delete_button.grid(row=5,column=1)
exit_button=Button(text="exit",fg="black",bg="green",font=("arial",10,"bold"),width=10, padx=16, pady=14,bd=7,justify=RIGHT,command=exit)
exit_button.grid(row=6,column=1)
view_button=Button(text="view",fg="black",bg="green",font=("arial",10,"bold"),width=10, padx=16, pady=14,bd=7,justify=LEFT, command=dview)
view_button.grid(row=6,column=0)
update_button=Button(text="update",fg="black",bg="green",font=("arial",10,"bold"),width=10, padx=16, pady=14,bd=7,justify=LEFT,command=edit)
update_button.grid(row=7,column=1)

time_label=Label(root,text=tim,fg='red',justify=CENTER)
time_label.grid(row=7,column=0)
root.mainloop()