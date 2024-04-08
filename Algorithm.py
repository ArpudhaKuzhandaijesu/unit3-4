#!/usr/bin/env python
# coding: utf-8

# In[2]:


#LINEAR SEARCH
def linear_search(arr,data):
    for i in range(len(arr)):
        if arr[i]==data:
            return i
    return -1
arr=[100,56,45,65,90]
data=65
ans=linear_search(arr,data)
if ans!= -1:
    print(f'array element found at {ans} position')
else:
    print("array element not found")


# In[19]:


#SORTING
def sort(arr):
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i]>arr[j]:   # "<"-for descending
                arr[i],arr[j]=arr[j],arr[i]
arr=[100,56,45,65,90]
res=sort(arr)
print(arr)


# In[6]:


#BINARY SEARCH
#insering data
data=[16,21,15,7,8,24,9,1,30,10,25,13,26,11,2,5,20,28,18,3]

#data sorting:
data.sort()

#printing sorted data:
print(data)

#reading search element:
elem=int(input("enter the search element:"))

#program:
def binary_search(data,elem):
    low=0
    high=len(data)-1
    while low<=high:
        middle=(low+high)//2
        if data[middle]==elem:
            print(f'the searching element {elem} is present in index value {middle} in database')
            break
        elif data[middle]>elem:
            high=middle-1
        else:
            low=middle+1
    if data[middle] != elem:
        print(f'the searching element {elem} is not present in the database')
        return -1

#function calling
binary_search(data,elem)


# BFS-breadth first search
# DNS-depth first search

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




