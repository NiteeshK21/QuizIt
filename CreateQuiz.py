from tkinter import *
from tkinter import ttk
import csv
import time
from PIL import ImageTk, Image

def get_Questions(user,qname,num,Time):
    file = open(f"Data/{qname}.csv",'a+')
    quesc=Tk()
    quesc.title("EnterQuestions")
    quesc.geometry("500x300")
    quesc.resizable(False,False)

    img=ImageTk.PhotoImage(Image.open("x.jpg"),master=quesc)
    bg_label=Label(quesc,image=img)
    bg_label.pack()

    quiz=Label(quesc,text=f"Quiz {qname}",font=("Algerian",15)).place(x=195,y=20)
    Question=Label(quesc,text="Enter Question").place(x=50,y=70)
    question=StringVar()
    Quest_entry=Entry(quesc,textvariable=question).place(x=190,y=70)
    OptionsList=["2 options","3 options","4 options","5 options","None"]
    OptionSelected=StringVar(quesc)
    OptionSelected.set("Select")
    question_menu = OptionMenu(quesc, OptionSelected, *OptionsList)
    question_menu.place(x=250,y=160)
    question_menu.config(height=1,bg='light blue')





    home_button = Button(quesc,text = "QuizIt",command=lambda: [quesc.destroy(),Welcome(user)],bg='grey',fg='white').place(x = 2,y = 2)    
    quesc.mainloop()
def Welcome(user):
    win=Tk()
    win.title("Welcome")
    win.geometry("500x300")
    win.resizable(False, False)
    bg=ImageTk.PhotoImage(Image.open("x.jpg"),master=win)
    blabel = Label(win, image=bg)
    blabel.pack()
    user=Label(win,text=f"Welcome {user}!").place(x=190,y=60)
    host_button = Button(win,text = "Host a Quiz",command=lambda: [win.destroy(),hostQuiz(user)]).place(x = 140,y = 90)
    join_button = Button(win,text = "Join a Quiz").place(x = 260,y = 90)
    win.mainloop()

    
def hostQuiz(user):
    def quizDetails(user):
        QuizName=quizName.get()
        numQuestions=str(nQuestions.get())
        Time=OptionSelected.get()
        if(len(QuizName)==0 or len(numQuestions)==0 or Time=="Select"):
            invalid=Label(root,text = "Invalid Credentials. Please Try Again.",font=(25),fg='red').place(x=100,y=240)
            root.after(2000,lambda:root.destroy())
            root.mainloop()
            hostQuiz(user)
        elif(not(numQuestions.isnumeric()) or int(numQuestions)<=0):
            invalid=Label(root,text="Invalid Input! Enter a positive integer.",font=(25),fg='red').place(x=190,y=141)
            root.after(2000,lambda:root.destroy())
            root.mainloop()
            hostQuiz(user)
        else:
            fields=["QNo.","Question","Time","Option1","Option2","Option3","Option4","CorrectAns","Explaination"]
            file=open(f"Data/{QuizName}.csv","w")
            writer=csv.writer(file)
            head=["","","",QuizName,"TimeRestriction:",Time]
            writer.writerow(head)
            writer.writerow(fields)
            file.close()
            root.destroy()
            get_Questions(user,QuizName,numQuestions,Time)

    root=Tk()
    root.title("CreateQuiz")
    root.geometry("500x300")
    root.resizable(False, False)

    bg=ImageTk.PhotoImage(Image.open("x.jpg"),master=root)
    background_label = Label(root, image=bg)
    background_label.pack()

    qname=Label(root,text="Enter Quiz Name",height=1).place(x=50,y=70)
    quizName=StringVar()
    quiz_name=Entry(root,textvariable=quizName,width=15).place(x=250,y=70)

    num_Questions=Label(root,text="Number of Questions",height=1).place(x=50,y=118)
    nQuestions=StringVar()
    quiz_name=Entry(root,textvariable=nQuestions,width=15)
    quiz_name.place(x=250,y=118)

    time=Label(root,text="Select time restriction",height=1).place(x=50,y=165)
    OptionsList=["Time limit per question","Time limit for the whole quiz","No time restriction"]
    OptionSelected=StringVar(root)
    OptionSelected.set("Select")
    question_menu = OptionMenu(root, OptionSelected, *OptionsList)
    question_menu.place(x=250,y=160)
    question_menu.config(height=1,bg='light blue')

    next_button = Button(root,text = "Next",fg="black",bg='grey',command=lambda: quizDetails(user)).place(x = 210,y = 210)

    home_button = Button(root,text = "QuizIt",command=lambda: [root.destroy(),Welcome(user)]).place(x = 10,y = 10)
    root.mainloop()

# Welcome("Niteesh")
# get_Questions("Niteesh","Try1","5","Time limit per question")

