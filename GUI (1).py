#!/usr/bin/env python
# coding: utf-8

# TKINTER

# In[10]:


import tkinter as tk
root=tk.Tk() #root window
#root.mainloop() #execute root window
#root.title('welcome') #changing root window name
#root.mainloop() # call root window repeatetly
#root.geometry("700x500")
#root.mainloop()


# In[11]:


mylabel=tk.Label(root,text="hello world") #create label
mylabel.pack() # insert label in root window
root.mainloop()


# In[116]:


myButton=tk.Button(root,text="click on")
myButton.pack()
#root.mainloop()


# In[117]:


myButton=tk.Button(root,text="click on")
myButton.place(x=50,y=100)
#root.mainloop()                      


# In[118]:


myButton=tk.Button(root,text="click on",padx=5,pady=5,bg="black",fg="white")
myButton.place(x=50,y=100)
#root.mainloop()


# In[112]:


import tkinter as tk
root=tk.Tk()
myButton=tk.Button(root,text="click on",padx=5,pady=5,bg="black",fg="white")
myButton.grid(row=1,column=3)
#root.mainloop()


# In[1]:


import tkinter as tk
root=tk.Tk()
myButton=tk.Button(root,text="click on",padx=5,pady=5,bg='black',fg='white').grid(row=0,column=0)
myButton=tk.Button(root,text="click on",padx=5,pady=5,bg='black',fg='white').grid(row=1,column=1)
root.mainloop()


# CLICKING ON A BUTTON

# In[128]:


import tkinter as tk
root=tk.Tk()
def myclick():
    mylabel=tk.Label(root,text="clicked on button")
    mylabel.pack()


# In[129]:


myButton=tk.Button(root,text="click me",command=myclick)
myButton.pack()
root.mainloop()


# In[11]:


import tkinter as tk
root=tk.Tk()
def green():
    label1=tk.Label(root,text="go")
    label1.pack()


# In[12]:


button1=tk.Button(root,text="green",command=green)
button1.pack()


# In[13]:


def yellow():
    label2=tk.Label(root,text="wait")
    label2.pack()
button2=tk.Button(root,text="yellow",command=yellow)
button2.pack()


# In[14]:


def red():
    label3=tk.Label(root,text="stop")
    label3.pack()
button3=tk.Button(root,text="red",command=red)
button3.pack()
root.mainloop()


# ENTRY WIDGETS:
# it is used to input single line text entry from user

# In[21]:


#import tkinter library module
import tkinter as tk


# In[22]:


#create root window by accessing Tk()class from tkinter
root=tk.Tk()


# In[23]:


#create entry widget in root window by using Entry() function
entrywidget=tk.Entry(root)


# In[24]:


#get text entry using insert() function
entrywidget.insert(0,"type ur text here")


# In[25]:


entrywidget.place(x=50,y=100) # or entrywidget.grid(row=0,column=1)
root.mainloop()


# RADIOBUTTON WIDGET:
# it is used to implement one of many selection as it allows only one option to be selected

# In[31]:


import tkinter as tk


# In[32]:


root=tk.Tk()
v=tk.IntVar() # corresponing integer value will be assigned once the button clicked on
v.set(1) #initialising the choice #the first choice wil be selcted as default as 1 is given inside the brackets


# In[33]:


radiobutton_widget1=tk.Radiobutton(root,
                                  text="radiobutton 1",
                                  variable=v,value=1)
radiobutton_widget2=tk.Radiobutton(root,
                                  text="radiobutton 2",
                                  variable=v,value=2)


# In[34]:


radiobutton_widget1.pack()
radiobutton_widget2.pack()


# In[35]:


root.mainloop()


# CHECK BUTTON:

# In[44]:


import tkinter as tk
root=tk.Tk()
root.geometry('400x400')
checkvar=tk.IntVar()
checkbtn=tk.Checkbutton(root,text="i agree",variable=checkvar,onvalue=1,offvalue=0,width=5)
checkbtn.pack()
root.mainloop()


# In[55]:


import tkinter as tk
root=tk.Tk()
label1=tk.Label(root,text="user name")
label1.place(x=60,y=100)
label2=tk.Label(root,text="password")
label2.place(x=60,y=130)


# In[56]:


ew=tk.Entry(root)
ew.insert(0,"type ur user name")
ew.place(x=150,y=100)
ew1=tk.Entry(root)
ew1.insert(0,"type ur password")
ew1.place(x=150,y=130)
v=tk.IntVar()
rw1=tk.Radiobutton(root,
                        text="male",
                        variable=v,value=1)
rw2=tk.Radiobutton(root,
                        text="female",
                        variable=v,value=2)
rw1.place(x=150,y=160)
rw2.place(x=150,y=190)
#root.geometry('400x400')
checkvar=tk.IntVar()
checkbtn=tk.Checkbutton(root,text="informtion given is correct",variable=checkvar,onvalue=1,offvalue=0,width=30)
checkbtn.place(x=130,y=220)
def submit():
    l=tk.Label(root,text="the above informations is submitted successfully")
    l.pack()
b=tk.Button(root,text="submit",command=submit)
b.place(x=150,y=250)
root.mainloop()


# CREATING LIST BOX:

# In[72]:


import tkinter as tk
root=tk.Tk()


# In[73]:


listbox=tk.Listbox(root)
list_entries=["new","open","save","save as"]


# In[74]:


for entry in list_entries:
    listbox.insert(tk.END,entry)
listbox.pack()


# In[75]:


root.mainloop()


# In[82]:


import tkinter as tk
root=tk.Tk()


# In[83]:


listbox=tk.Listbox(root)
list_entries=["new","open","save","save as"]
def list():
    for entry in list_entries:
        listbox.insert(tk.END,entry)
    listbox.place(x=100,y=150)


# In[84]:


button=tk.Button(root,text="file",command=list)
button.place(x=100,y=50)
root.mainloop()


# CREATING MENU BAR:

# In[137]:


import tkinter as tk
root=tk.Tk()


# In[138]:


def menu_callback():
    print("i am in main menu")
def submenu_callback():
    print("i am in sub menu")


# In[139]:


menu=tk.Menu(root)


# In[140]:


submenu=tk.Menu(menu)
submenu.add_command(label="new",command=submenu_callback)
submenu.add_command(label="open",command=submenu_callback)
submenu.add_command(label="save",command=submenu_callback)
submenu.add_command(label="save as",command=submenu_callback)
submenu.add_command(label="exit",command=submenu_callback)


# In[141]:


menu.add_cascade(label="file",menu=submenu)


# In[142]:


root.config(menu=menu)


# In[148]:


menu1=tk.Menu(root)
submenu1=tk.Menu(menu1)
submenu1.add_command(label="undo",command=submenu_callback)
submenu1.add_command(label="redo",command=submenu_callback)
submenu1.add_command(label="cut",command=submenu_callback)
submenu1.add_command(label="copy",command=submenu_callback)
submenu1.add_command(label="paste",command=submenu_callback)
menu1.add_cascade(label="edit",menu1=submenu1)
root.config(menu=menu1)


# In[144]:


root.mainloop()


# IMAGE READING:

# In[2]:


pip install Pillow


# In[4]:


pip show pillow


# In[16]:


import tkinter as tk
from PIL import ImageTk,Image
root=tk.Tk()
root.title("image viewer")
image_path="C:\Users\aedpu\OneDrive\Pictures"
image=Image.open(image_path)
tk_image=ImageTk.photoImage(image)
label=tk.Label(root,image=tk_image)
label.pack()
root.mainloop()


# MESSAGE BOX:

# In[12]:


import tkinter as tk 
from tkinter import messagebox

def show_info_message(): #( message box name , text that is displayed inside the box)
    messagebox.showinfo("information","this is an information message")

def show_warning_message():
    messagebox.showwarning("warning","this is a warning message")

def show_error_message():
    messagebox.showerror("error","this is error message")

def ask_question():
    responce=messagebox.askquestion("question","do you like python")
    messagebox.showinfo("responce",f"you answered:{responce}")

def ask_ok_cancel():
    responce=messagebox.askokcancel("confirmation","are you sure you want to proceed")
    if responce:
        messagebox.showinfo("confirmation","you clicked ok")
    else:
        messagebox.showinfo("confirmation","you clicked cancel")

def ask_yes_no():
    responce=messagebox.askyesno("confirmation","are you sure you want to proceed")
    if responce:
        messagebox.showinfo("confirmation","you clicked ok")
    else:
        messagebox.showinfo("confirmation","you clicked cancel")

root=tk.Tk()
root.title("message box")
info_button=tk.Button(root,text="show info message",command=show_info_message)
info_button.pack(pady=5)

warning_button=tk.Button(root,text="show warning message",command=show_warning_message)
warning_button.pack(pady=5)

error_button=tk.Button(root,text="show error message",command=show_error_message)
error_button.pack(pady=5)

ask_button=tk.Button(root,text="show ask quesion",command=ask_question)
ask_button.pack(pady=5)

ok_cancel_button=tk.Button(root,text="show ok or cancel message",command=ask_ok_cancel)
ok_cancel_button.pack(pady=5)

yes_no_button=tk.Button(root,text="show yes or no message",command=ask_yes_no)
yes_no_button.pack(pady=5)

root.mainloop()


# In[14]:


import tkinter as tk 
from tkinter import messagebox
def ask_ok_cancel():
    responce=messagebox.askokcancel("confirmation","are you sure you want to close the tab")
    if responce:
        messagebox.showinfo("confirmation","you clicked ok \n the tab will be closed")
    else:
        messagebox.showinfo("confirmation","you clicked cancel \n you can continue")
root=tk.Tk()
root.title("message box")
ok_cancel_button=tk.Button(root,text="show ok or cancel message",command=ask_ok_cancel)
ok_cancel_button.pack(pady=5)    
root.mainloop()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




