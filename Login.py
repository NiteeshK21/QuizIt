from tkinter import *
from tkinter import ttk
import csv
import time
import CreateQuiz as cq
from PIL import ImageTk, Image

def SignUP():
    root=Tk()
    root.title("SignUp")
    root.geometry("450x300")
    def add(user,passw):
        f=open("Data/users.csv",'a+')
        rows=[]
        csvwriter=csv.writer(f)
        f.seek(0)
        lines=f.readlines()
        for i in lines:
            rows.append(list(i.split(",")))
        for j in rows:
            if(j[0]==user):
                top=Tk()
                top.title("Invalid")
                top.geometry("450x200")
                exists = Label(top,text = "Username already exists! Please try a different one.").place(x = 40,y = 60)
                top.after(2000,lambda:top.destroy())
                top.mainloop()
                SignUP()
                return
        data=[user,passw]
        csvwriter.writerow(data)
        f.close()
        added = Label(root,text = "User added successfully!").place(x = 40,y = 170)
        root.after(2000,lambda:root.destroy())
        root.mainloop()
        login()
        
    def get_data():
        user=str(userdata.get())
        password=str(pass_data.get())
        if(len(user)==0 or len(password)==0):
            invalid = Label(root,text = "Username or password cannot be empty!").place(x = 40,y = 170) 
            root.after(2000,lambda:root.destroy())
            root.mainloop()
            SignUP()
        else:
            add(user,password)
    user_name = Label(root,text = "Username").place(x = 40,y = 60)    
    user_password = Label(root,text = "Password").place(x = 40,y = 100)
    userdata=StringVar()
    user_name_input = Entry(root,textvariable=userdata,width = 30).place(x = 120,y = 60)
    pass_data=StringVar()
    password_entry = Entry(root,textvariable=pass_data,width = 30).place(x = 120,y = 100)
    signup_button = Button(root,text = "Sign Up",command=get_data).place(x = 40,y = 130)
    root.mainloop()
    
def authenticate(user,passw):
    fields=[]
    rows=[]
    with open("Data/users.csv","r") as csvfile:
        csvreader=csv.reader(csvfile)
        fields=next(csvreader)
        for row in csvreader:
            rows.append(row)
        for row in rows:
            if(row[0]==user and row[1]==passw):
                cq.Welcome(user)
                return
        root=Tk()
        invalid=Label(root,text = "Invalid Credentials. Please Try Again.",font=(25))
        invalid.pack()
        root.after(2000,lambda:root.destroy())
        root.mainloop()
        login()

def login():
    top = Tk()
    top.geometry("450x300")
    img=ImageTk.PhotoImage(Image.open("x.jpg"),master=top)
    bg_label=Label(top,image=img)
    bg_label.pack()
    def get_data():
        user=userdata.get()
        password=pass_data.get()
        top.destroy()
        authenticate(user,password)
    user_name = Label(top,text = "Username").place(x = 40,y = 60)
    userdata=StringVar()
    user_name_input = Entry(top,textvariable=userdata,width = 30).place(x = 120,y = 60)

    user_password = Label(top,text = "Password").place(x = 40,y = 100)
    pass_data=StringVar()
    password_input = Entry(top,textvariable=pass_data,width = 30).place(x = 120,y = 100)
    
    submit_button = Button(top,text = "Submit",command=get_data).place(x = 40,y = 130)
    signup_button = Button(top,text = "Don't have an account? SignUp",command=lambda: [top.destroy(),Signup()]).place(x = 200,y = 130)
    top.mainloop()
login()
