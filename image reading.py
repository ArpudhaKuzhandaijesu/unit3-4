#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install Pillow


# In[2]:


pip show pillow


# In[1]:


import tkinter as tk
from PIL import ImageTk,Image
root=tk.Tk()
root.title("image viewer")

image_path="C:\\Users\\aedpu\\OneDrive\\Pictures\\flower.jpg"
image=Image.open(image_path)

tk_image=ImageTk.PhotoImage(image)

label=tk.Label(root,image=tk_image)
label.pack()
root.mainloop()


# In[6]:


from tkinter import *
root=Tk()
root.geometry("200x200")
def open():
    top=Toplevel(root)
    top.mainloop()
btn=Button(root,text="open",command=open)
btn.place(x=75,y=50)
root.mainloop()


# In[ ]:





# In[ ]:




