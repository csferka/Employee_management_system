from customtkinter import *
from PIL import Image
from tkinter import ttk,messagebox
import database


#functions
def delete_all():
    result=messagebox.askyesno("Confirm","Do you really want to delete all records?")
    if result:
        database.deleteall_records()
    else:
        pass


def show_all():
    treeview_data()
    searchEntry.delete(0,END)
    searchcombo.set("Search By")
def search_employee():
    if searchEntry.get()=="":
        messagebox.showerror("Error","Enter value to search")
    elif searchcombo.get()=='Search By':
        messagebox.showerror("Error","Please select an option")
    else:
        searchdata=database.search(searchcombo.get(),searchEntry.get())
        tree.delete(*tree.get_children())
        for employee in searchdata:
            tree.insert('',END,values=employee)


def delete_employee():
    selected_item=tree.selection()
    if not selected_item:
        messagebox.showerror("Error","Items not selected to delete")
    else:
        database.delete(idEntry.get())
        treeview_data()
        clear()
        messagebox.showinfo("Success","Data is deleted")


def employee_update():
    selected_item=tree.selection()
    if not selected_item:
        messagebox.showerror("Error","Items not selected to update")
    else:
        database.update(idEntry.get(),nameEntry.get(),phoneEntry.get(),Rolecombo.get(),Gendercombo.get(),salaryEntry.get())
        treeview_data()
        clear()
        messagebox.showinfo("Success","Data is Updated!")


def selection(event):
    selected_item=tree.selection()
    if selected_item:
        clear()
        row=tree.item(selected_item)['values']
        idEntry.insert(0,row[0])
        nameEntry.insert(0,row[1])
        phoneEntry.insert(0,row[2])
        Rolecombo.set(row[3])
        Gendercombo.set(row[4])
        salaryEntry.insert(0,row[5])


def clear(value=False):
    if value:
        tree.selection_remove(tree.focus())
    idEntry.delete(0,END)
    phoneEntry.delete(0,END)
    salaryEntry.delete(0,END)
    nameEntry.delete(0,END)
    Rolecombo.set('Web developer')
    Gendercombo.set('Male')
def treeview_data():
    employees=database.fetch_employees()
    tree.delete(*tree.get_children())
    for employee in employees:
        tree.insert('',END,values=employee)
def add_employee():
    if idEntry.get()=="" or nameEntry.get()=="" or salaryEntry.get()=="" or phoneEntry=="":
        messagebox.showerror(title="Error",message="all fields should be filled")

    elif database.id_exists(idEntry.get()):
        messagebox.showerror(title="Error",message="Id already exists")

    else:
        database.insert(idEntry.get(),nameEntry.get(),phoneEntry.get(),Rolecombo.get(),Gendercombo.get(),salaryEntry.get())
        treeview_data()
        clear()
        messagebox.showinfo("Success",'Data is added')

#gui part
set_appearance_mode('light')
window=CTk(fg_color="white")



window.geometry("1200x650+100+100")
window.resizable(False,False)
window.title("Employee management system")
window.configure(fg_color="#161C30")

leftFrame=CTkFrame(window)
leftFrame.grid(row=1,column=0)

leftFrame = CTkFrame(window,fg_color="#161C30")
leftFrame.grid(row=1, column=0, padx=20, pady=20)  # Added padding for better spacing

# ID Label and Entry
idLabel = CTkLabel(leftFrame, text='Id', font=('Goudy Old Style', 20, 'bold'), text_color='white')
idLabel.grid(row=0, column=0, padx=20, pady=15, sticky='w')  # Added padx
idEntry = CTkEntry(leftFrame, placeholder_text="",  placeholder_text_color='white', width=180)
idEntry.grid(row=0, column=1, pady=15)

# Name Label and Entry
nameLabel = CTkLabel(leftFrame, text='Name', font=('Goudy Old Style', 20, 'bold'), text_color='white')
nameLabel.grid(row=1, column=0, padx=20, sticky='w')
nameEntry = CTkEntry(leftFrame, placeholder_text="",  placeholder_text_color='white', width=180)
nameEntry.grid(row=1, column=1)

# Phone Label and Entry
phoneLabel = CTkLabel(leftFrame, text='Phone', font=('Goudy Old Style', 20, 'bold'), text_color='white')
phoneLabel.grid(row=2, column=0, padx=20, pady=15, sticky='w')
phoneEntry = CTkEntry(leftFrame, placeholder_text="",  placeholder_text_color='white', width=180)
phoneEntry.grid(row=2, column=1, pady=15)

# Role Label and ComboBox (Fixed variable name)
roleLabel = CTkLabel(leftFrame, text='Role', font=('Goudy Old Style', 20, 'bold'), text_color='white')
roleLabel.grid(row=3, column=0, padx=20, pady=15, sticky='w')  # Changed row from 4 → 3
Roleoptions = ["Web Developer", "UX/UI Designer", "Cloud Architect", "Network Engineer", "Data Scientist"]
Rolecombo = CTkComboBox(leftFrame, values=Roleoptions, fg_color="white", text_color="black", width=180)
Rolecombo.grid(row=3, column=1, pady=15)  # Changed row from 4 → 3

# Gender Label and ComboBox (Fixed incorrect values)
genderLabel = CTkLabel(leftFrame, text='Gender', font=('Goudy Old Style', 20, 'bold'), text_color='white')
genderLabel.grid(row=4, column=0, padx=20, pady=15, sticky='w')  # Changed row from 5 → 4
Genderoptions = ["Male", "Female"]
Gendercombo = CTkComboBox(leftFrame, values=Genderoptions, fg_color="white",width=180, text_color="black")  # Fixed incorrect values
Gendercombo.grid(row=4, column=1, padx=20, pady=15)  # Changed row from 5 → 4

# Salary Label and Entry
salaryLabel = CTkLabel(leftFrame, text='Salary', font=('Goudy Old Style', 20, 'bold'), text_color='white')
salaryLabel.grid(row=5, column=0, padx=20, pady=15, sticky='w')  # Changed row from 6 → 5
salaryEntry = CTkEntry(leftFrame, placeholder_text="",  placeholder_text_color='white', width=180)
salaryEntry.grid(row=5, column=1, padx=20, pady=15)  # Changed row from 6 → 5


rightFrame=CTkFrame(window,fg_color="white")
rightFrame.grid(row=1,column=1)

logo=CTkImage(Image.open('bg.png'),size=(1200,200))
imageLabel=CTkLabel(window,image=logo,text='')
imageLabel.grid(row=0,column=0,columnspan=2)


searchoptions = ["Name", "Id","Salary","Role","Gender","Phone"]
searchcombo = CTkComboBox(rightFrame,values=searchoptions,text_color="black",state='readonly')  # Fixed incorrect values
searchcombo.set("Search By")
searchcombo.grid(row=0, column=0,padx=15)  # Changed row from 5 → 4

searchEntry = CTkEntry(rightFrame)
searchEntry.grid(row=0, column=1,padx=15)  # Changed row from 6 → 5

searchButton=CTkButton(rightFrame,text='Search',border_color='blue',cursor='hand2',command=search_employee)
searchButton.grid(row=0,column=2,padx=15)

showButton=CTkButton(rightFrame,text='Show All',border_color='blue',cursor='hand2',command=show_all)
showButton.grid(row=0,column=3,padx=15)

tree=ttk.Treeview(rightFrame,height=18)
tree.grid(row=1,column=0,columnspan=4)

tree['columns']=('Id','Name','Phone','Role','Gender','Salary')

tree.heading('Id',text='Id')
tree.heading('Name',text='Name')
tree.heading('Phone',text='Phone')
tree.heading('Role',text='Role')
tree.heading('Gender',text='Gender')
tree.heading('Salary',text='Salary')

tree.config(show='headings')
tree.column('Id',anchor=CENTER,width=50)
tree.column('Name',anchor=CENTER,width=100)
tree.column('Phone',anchor=CENTER,width=150)
tree.column('Role',anchor=CENTER,width=150)
tree.column('Gender',anchor=CENTER,width=100)
tree.column('Salary',anchor=CENTER,width=100)

style=ttk.Style()
style.configure('Treeview.Heading',font=('arial',18,'bold'))
style.configure('Treeview',font=('arial',15,'bold'),background='#161C30',foreground='white')

scrollbar=ttk.Scrollbar(rightFrame,orient=VERTICAL,command=tree.yview)
scrollbar.grid(row=1,column=4,sticky='ns')


buttonFrame=CTkFrame(window,fg_color="#161C30")
buttonFrame.grid(row=2,column=0,columnspan=2)

newButton=CTkButton(buttonFrame,text='New Employee',font=('arial',15,'bold'),width=160,corner_radius=15,command=lambda: clear(True))
newButton.grid(row=0,column=0,pady=5,padx=10)

addButton=CTkButton(buttonFrame,text='Add Employee',font=('arial',15,'bold'),width=160,corner_radius=15,command=add_employee)
addButton.grid(row=0,column=1,pady=5,padx=10)

updateButton=CTkButton(buttonFrame,text='Update Employee',font=('arial',15,'bold'),width=160,corner_radius=15,command=employee_update)
updateButton.grid(row=0,column=2,padx=10)

deleteButton=CTkButton(buttonFrame,text='Delete Employee',font=('arial',15,'bold'),width=160,corner_radius=15,command=delete_employee)
deleteButton.grid(row=0,column=3)


deleteallButton=CTkButton(buttonFrame,text='Delete All',font=('arial',15,'bold'),width=160,corner_radius=15,command=delete_all)
deleteallButton.grid(row=0,column=4,padx=10)

treeview_data()
window.bind('<ButtonRelease>',selection)
window.mainloop()

