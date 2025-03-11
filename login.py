from customtkinter import *
from PIL import Image
from tkinter import messagebox

def login():
    if usernameEntry.get()=='' or passwordEntry=='':
        messagebox.showerror('Error','All fields are required to fill')
    elif usernameEntry.get()=='feruz' and passwordEntry.get()=='1234':
        messagebox.showinfo('Success',"Login is successful")
        root.destroy()
        import ems
    else:
        messagebox.showerror('Error','wrong cridentials')


set_appearance_mode('light')
root=CTk(fg_color="white")
root.geometry("760x360")
root.resizable(0,0)
root.title("login page")

image=CTkImage(Image.open('Background.jpg'),size=(760,360))
imageLabel=CTkLabel(root,image=image,text='')
imageLabel.place(x=0,y=0)

headingLabel=CTkLabel(root,text='Employee Management System',bg_color='#6CE6E0',font=('Goudy Old Style',20,'bold'),text_color='dark blue')
headingLabel.place(x=20,y=100)


usernameEntry=CTkEntry(root,placeholder_text="Enter your username",bg_color='white',placeholder_text_color='white',width=180)
usernameEntry.place(x=50,y=150)

passwordEntry=CTkEntry(root,placeholder_text="Enter your password",bg_color='white',placeholder_text_color='white',width=180 ,show="*")
passwordEntry.place(x=50,y=200)

loginButton=CTkButton(root,text='Login',border_color='blue',cursor='hand2',command=login)
loginButton.place(x=70,y=250)

root.mainloop()
