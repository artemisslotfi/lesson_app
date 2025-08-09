from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from warnings import showwarning
import re

lesson_list=[]


def code_validator(code):
    if re.match(r"^[a-zA-Z\d\s]{3,30}$",code):
        return True
    else:
        return False

def title_validator(title):
    if re.match(r"^[a-zA-Z\s]{3,30}$",title):
        return True
    else:
        return False


# 5
def reset_form():
    code.set("")
    title.set("")
    teacher.set("")
    class_number.set("")
    unit.set(0)


# 6
def save_click():
    if code_validator(code.get()) and title_validator(title.get()) and title_validator(teacher.get()) and code_validator(class_number.get()) and 0<unit.get()<=24:
        lesson={
            "code":code.get(),
            "title":title.get(),
            "teacher":teacher.get(),
            "class number":class_number.get(),
            "unit":unit.get(),
        }
        lesson_list.append(lesson)
        messagebox.showinfo("Save", f"Successfully saved!\n{lesson}")
        reset_form()

        table.insert("",END,values=tuple(lesson.values( )))
    else:
        messagebox.showerror("Error", "Please enter a valid code/title/teacher/class number/unit")

# HomeWork
def edit_click():
    selected_item=table.focus()
    if selected_item=="":
        return messagebox.showwarning("Warning", "Please select a lesson")
    new_data=(code.get(),title.get(),teacher.get(),class_number.get(),unit.get())
    if code.get()!="" and title.get()!="" and teacher.get()!="" and class_number.get()!="" and unit.get()!="":
        table.item(selected_item,values=new_data)
        reset_form()
    else:
        return showwarning("Warning","لطفا همه ی فیلد هارو پر کنید")


def remove_click():
    selected_item = table.focus()
    if selected_item=="":
        return messagebox.showwarning("Warning", "Please select a lesson")
    if messagebox.askyesno("Delete", "Are you sure ?"):
        table.delete(selected_item)
        reset_form()


# 7
def table_select(event):
    table_row=table.focus()
    selected=table.item(table_row)["values"]
    code.set(selected[0])
    title.set(selected[1])
    teacher.set(selected[2])
    class_number.set(selected[3])
    unit.set(selected[4])


def close_window():
    if messagebox.askyesno("Exit", "Are you sure ?"):
        win.destroy()

# 0
win = Tk()
# geometry-title
win.title("Lesson")
win.resizable(width=False, height=False)
win.geometry("710x360")

# 1
# Code
code=StringVar()
Label(win,text="Code").place(x=20,y=20)
Entry(win, textvariable=code).place(x=100,y=20)

# Title
title=StringVar()
Label(win,text="Title").place(x=20,y=60)
Entry(win, textvariable=title).place(x=100,y=60)

# Teacher
teacher=StringVar()
Label(win,text="Teacher").place(x=20,y=100)
Entry(win, textvariable=teacher).place(x=100,y=100)
# Class Number
class_number=StringVar()
Label(win,text="Class Number").place(x=20,y=140)
Entry(win, textvariable=class_number).place(x=100,y=140)

# Unit
unit=IntVar()
Label(win,text="Unit").place(x=20,y=180)
Entry(win, textvariable=unit).place(x=100,y=180)

# 2
# Buttons (Save-Edit-Remove)
Button(win, text="Save", command=save_click, width=7).place(x=20,y=300)
Button(win, text="Edit", command=edit_click, width=7).place(x=95,y=300)
Button(win, text="Remove", command=remove_click, width=7).place(x=170,y=300)
# 3
# Search Title
title_search = StringVar()
Label(win,text="Search Title").place(x=250,y=20)
Entry(win, textvariable=title_search).place(x=325,y=20)

# Search Teacher
teacher_search = StringVar()
Label(win,text="Search Teacher").place(x=470,y=20)
Entry(win, textvariable=teacher_search).place(x=560,y=20)

# 4
# Table
table = ttk.Treeview(win, height=12,columns=(1,2,3,4,5),show="headings")
table.column(1, width=70)
table.column(2, width=100)
table.column(3, width=100)
table.column(4, width=80)
table.column(5, width=80)

table.heading(1, text="Code")
table.heading(2, text="Title")
table.heading(3, text="Teacher")
table.heading(4, text="Class Number")
table.heading(5, text="Unit")

# TreeviewSelect
# bind--> table_select
table.bind("<<TreeviewSelect>>", table_select)

table.place(x=250, y = 60)


win.protocol("WM_DELETE_WINDOW", close_window)


win.mainloop()