import tkinter 
#import tkinter=full name       import tkinter as tk means i give short form to tk      from tkinter import *= use names directly 
from tkinter import messagebox
window=tkinter.Tk()
window.title('LOGIN FORM')
window.geometry('740x740')
window.configure(bg="light blue")

frame=tkinter.Frame(bg='light blue')
def login():
    username='fatima'
    password='12128'
    if user_name.get()==username and password_wntry.get()==password:
        messagebox.showinfo(title='login success',message='you are successfully login')
    else:
        messagebox.showinfo(title='login error',message='invalid input.check username and password')

#making the loginpage
login_label=tkinter.Label(frame,text='Login ',bg="light blue",font=('arial',40,'bold'))
username_login=tkinter.Label(frame,text='Username: ',bg="light blue",font=('arial',20))
user_name=tkinter.Entry(frame,font=('arial',20),width=30)
password_login=tkinter.Label(frame,text='Password: ',bg="light blue",font=('arial',20))
password_wntry=tkinter.Entry(frame,show='*',font=('arial',20),width=30)  #show makes th text hidden as the user types
login_button=tkinter.Button(frame,text='Login',font=('arial',30,'bold'),command=login)

#setting on the screen 
login_label.grid(row=0,column=0,pady=60,columnspan=2)
username_login.grid(row=1,column=0,padx=15,pady=10,sticky='we')
user_name.grid(row=1,column=1,padx=15,sticky='w')
password_login.grid(row=2,column=0,padx=15,sticky='e',pady=10)
password_wntry.grid(row=2,column=1,pady=10,padx=15,sticky='w')
login_button.grid(row=3,column=0,pady=40,columnspan=2)

frame.pack()

window.mainloop()
