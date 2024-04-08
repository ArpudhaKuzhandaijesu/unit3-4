#!/usr/bin/env python
# coding: utf-8

# In[1]:


class bike:
    name="tata"
    year=2000
    def cardata(self):
        print(self.name,self.year)
b=bike()
    
        


# In[2]:


b.name


# In[3]:


b.name="bmw"


# In[4]:


b.name


# In[7]:


setattr(bike,"name","maruthi")


# In[9]:


getattr(bike,"name")


# In[40]:


class circle:
    def __init__(self,r,p):
        self.r=r
        self.p=p
    def area(self):
        return self.p*self.r*self.r
r=int(input("enter the value of radius:"))
p=3.14
cir=circle(r,p)
cir.area()


# In[36]:


class rec:
    def __init__(self,l,b):
        self.l=l
        self.b=b
    def area(self):
        return self.l*self.b
l=int(input("enter the length of rectangle"))
b=int(input("enter the breath of rectangle"))
r=rec(l,b)
r.area()


# DATA ENCAPTUALIZATION
# 1.PRIVATE
# 2.PUBLIC
# 3.PROTECTED

# In[44]:


#private
class vgames:
    def __init__(self):
        self.__name="coc"
    def name(self):
        print(self.__name)
g=vgames()
g.name()


# In[49]:


class vgames:
    def __init__(self):
        self.__name="coc"
    def __printname(self):
        print(self.__name)
    def printname1(self):
        self.__printname()
g=vgames()
g.printname1()


# In[ ]:


INHERITANCE

