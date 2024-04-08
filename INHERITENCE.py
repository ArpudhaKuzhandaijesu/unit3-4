#!/usr/bin/env python
# coding: utf-8

# INHERITENCE

# In[3]:


#single level inheritence
class father:
    def land(self):
        print("have own land")  #base class
class son(father):
    def bike(self):
        print("have own bike")   #derive class
f=son()
f.land()
f.bike()


# In[6]:


#multi level inheritence
class grandfather:
    def land(self):
        print("have own land")  #base class 1
class father(grandfather):
    def house(self):
        print("have own house")  #base class 2 / derive class 1
class son(father):
    def car(self):
        print("have own car")  #derive class 2
s=son()
s.land()
s.house()
s.car()


# In[12]:


#multiple inheritence
class grandfather:
    def land(self):
        print("have own land")  #base class 1
class father:
    def house(self):
        print("have own house")  #base class 2 / derive class 1
class child:
    def cycle(self):
        print("have own cycle")  #base class 3 / derive class 2
class son(father,grandfather,child):
    def car(self):
        print("have own car")  #derive class 3
s=son()
s.land()
s.house()
s.car()
s.cycle()


# In[17]:


#protected encaptualization
class grandfather:
    def _land(self):
        print("have own land")  #base class 1
class father():
    def house(self):
        print("have own house")  #base class 2 / derive class 1
class son(father,grandfather):
    def car(self):
        print("have own car")  #derive class 2
s=son()
s._land()
s.house()
s.car()


# In[28]:


#super method
class a:
    def __init__(self):
        print("A class")
class b(a):
    def __init__(self):
        super().__init__()
        print("B class")
class c(b,a):
    def __init__(self):
        super().__init__()
        #super().__init__()
        print("C class")
#A=a()
#B=b()
C=c()


# In[35]:


class animal:
    def sound(self):
        print("animals make sound")
class dog(animal):
    def sound(self):
        print("woof")
class cat(animal):
    def sound(self):
        print("meow")
d=dog()
c=cat()
d.sound()
c.sound()    


# In[37]:


class birds:
    def sound(self):
        print("birds chirps")
class crow(birds):
    def sound(self):
        print("ka ka")
class duck(birds):
    def sound(self):
        print("bak bak")
class cuckoo(birds):
    def sound(self):
        print("ku ku")
c=crow()
d=duck()
cu=cuckoo()
c.sound()
d.sound()
cu.sound()


# OPERATOR OVERRULE

# In[43]:


a=10
b=20
a+b


# In[41]:


A="hello"
B="world"
A+B


# In[50]:


class addition:
    def __init__(self,a):
        self.a=a
    def __add__(self,a):
        return A.a+B.a
    def __mul__(self,a):
        return A.a*B.a
A=addition(10)
B=addition(20)
c=A+B
m=A*B
print(c)
print(m)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




