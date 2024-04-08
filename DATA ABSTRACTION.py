#!/usr/bin/env python
# coding: utf-8

# DATA ABSTRACTION
# hide internal process

# In[9]:


from abc import ABC, abstractmethod
class bank(ABC):  #abstract class
    @abstractmethod    # @ -> decorator
    def credit(self):  #cannot create object for abstract class
        pass
    @abstractmethod
    def debit(self):
        pass

class sbi(bank):  #normal class
    def credit(self):
        print("sbi gives credit")
    def debit(self):
        print("sbi gives debit")

class iob(bank):  #normal class
    def credit(self):
        print("iob gives credit")
    def debit(self):
        print("iob gives debit")
    
s=sbi()
s.credit()
i=iob()
i.debit()


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





# In[ ]:




