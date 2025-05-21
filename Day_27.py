#!/usr/bin/env python
# coding: utf-8

# # Dictionary Methods
# Dictionary uses several built-in methods for manipulation.They are listed below
# ### update()
# The update() method updates the value of the key provided to it if the item already exists in the dictionary, else it creates a new key-value pair.

# In[9]:


sr1 = {'Name': 'Samarth','Age':45, 'Branch':'AI' }
sr2 = {'Last Name': 'More', 'DOB': '24-04-2003'}
sr1.update(sr2)
print(sr1)


# In[10]:


info = {'name':'Karan', 'age':19, 'eligible':True}
print(info)
info.update({'age':20})
info.update({'DOB':2001})
print(info)


# ## Removing items from dictionary:
# There are a few methods that we can use to remove items from dictionary.
# ### clear():
# The clear() method removes all the items from the list.

# In[11]:


info = {'name':'Karan', 'age':19, 'eligible':True}
info.clear()
print(info)


# ### pop():
# The pop() method removes the key-value pair whose key is passed as a parameter.

# In[15]:


emp = {'Name':'Samarth', 'Age':22, 'Branch':'AI'}
emp.pop("Branch")
print(emp)


# In[16]:


info = {'name':'Karan', 'age':19, 'eligible':True}
info.pop('eligible')
print(info)


# ### popitem():
# The popitem() method removes the last key-value pair from the dictionary.

# In[17]:


info = {'name':'Karan', 'age':19, 'eligible':True, 'DOB':2003}
info.popitem()
print(info)


# In[20]:


emp = {'Name':'Samarth','Age':22, 'Branch':'AI'}
emp.popitem()
print(emp)


# ### del:
# we can also use the del keyword to remove a dictionary item.

# In[23]:


info = {'name':'Karan', 'age':19, 'eligible':True, 'DOB':2003}
del info['age']
print(info)


# In[27]:


info = {'name':'Karan', 'age':19, 'eligible':True, 'DOB':2003}
del info
print(info)


# In[ ]:





# In[ ]:




