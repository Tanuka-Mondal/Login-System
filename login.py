from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
class Login:
    def __init__(self,root):
        self.root = root
        self.root.title("Login Portal")
        self.root.geometry("1199x600+100+50")

        self.bg=ImageTk.PhotoImage(file="login_image.webp")
        self.bg_image=Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)
        self.root.resizable(False,False)

        Frame_login = Frame(self.root, bg="pink")
        Frame_login.place(x=350,y=150,height=340,width=500)

        title=Label(Frame_login,text="Login Here",font=("Impact",35,"bold"),fg="#DF0174",bg="pink").place(x=90,y=30)
        description=Label(Frame_login,text="Student Login Area",font=("Times New Roman",15,"bold"),fg="#FE2E9A",bg="pink").place(x=90,y=100)

        label_user=Label(Frame_login,text="Username",font=("Times New Roman",15,"bold"),fg="gray",bg="pink").place(x=90,y=140)
        self.text_user=Entry(Frame_login,font=("arial",15),bg="lightgray")
        self.text_user.place(x=90,y=170,height=35,width=350)

        label_password=Label(Frame_login,text="Password",font=("Times New Roman",15,"bold"),fg="gray",bg="pink").place(x=90,y=210)
        self.text_password=Entry(Frame_login,font=("arial",15),bg="lightgray",show="*")
        self.text_password.place(x=90,y=240,height=35,width=350)

        forget_button=Button(Frame_login,text="Forget Password?",cursor="hand2",bg="pink",bd=0,fg="#FE2E9A",font=("Times New Roman",12)).place(x=90,y=280)
        login_button=Button(self.root,command=self.login_function,cursor="hand2",text="Login",fg="pink",bg="#DF0174",font=("Times New Roman",20,"bold")).place(x=510,y=470,width=180,height=40)

    def login_function(self):
        if self.text_password.get()=="" or self.text_user.get()=="":
            messagebox.showerror("Error","All fields are required", parent=self.root)
        elif self.text_user.get()!="Tanuka" or self.text_password.get()!="abcd1234":
            messagebox.showerror("Error","Invalid Username or Password", parent=self.root)    
        else:
            messagebox.showinfo("Welcome",f"Welcome {self.text_user.get()}\nYou have successfully logged in!")    



root = Tk()   
obj = Login(root)
root.mainloop()
