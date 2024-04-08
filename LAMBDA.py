#!/usr/bin/env python
# coding: utf-8

# In[1]:


list=[1,2,3,4,5]
a=lambda x,y,z: x+y+z
b=lambda l:l%2==0
print(a)


# In[2]:


a(1,5,6)


# In[3]:


b(4)


# In[4]:


b(9)


# In[8]:


add=lambda r,a,s,k :r+a+s+k


# In[9]:


add


# In[10]:


add(1,2,3,4)


# In[11]:


mul=lambda r,a,s,k: r*a*s*k


# In[12]:


mul


# In[13]:


mul(1,2,3,4)


# In[14]:


add=lambda r,a :r+a


# In[15]:


add


# In[16]:


add(1,2)


# In[17]:


x=lambda a,b: (a^2)+(b^2)-(2^a*b)
#(1^2)+(2^2)-(2^1*2)
#1+4-4=1


# In[19]:


y=int(input("emter the number"))
z=int(input("enter the number"))
x(y,z)


# In[20]:


x=lambda a,b,c : (a^3)+(b^3)+(3^a+b*b+c*c+a)


# In[22]:


y=int(input("emter the number"))
z=int(input("emter the number"))
n=int(input("emter the number"))
x(y,z,n)


# In[23]:


k=(10,20,30,40,50)


# In[32]:


map1=map (lambda s : s*s,k)


# In[33]:


map1


# In[34]:


list(map1)


# In[27]:


filter1=filter(lambda r: r%2==0,map1)


# In[28]:


list(filter1)


# In[35]:


map


# In[36]:


s=[34,56,77,99,12]


# In[37]:


map1=map (lambda a : a*a,s)


# In[38]:


map1


# In[39]:


list(map1)


# In[40]:


filter2=filter(lambda r: r%2==0,map1)


# In[41]:


list(filter2)


# In[ ]:




