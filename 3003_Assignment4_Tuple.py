#!/usr/bin/env python
# coding: utf-8

# ### Q1) Reverse the following tuple
# ### aTuple = (10, 20, 30, 40, 50,60)
# 

# In[1]:


aTuple = (10, 20, 30, 40, 50, 60)

reversed_tuple = aTuple[::-1]

print(reversed_tuple)


# In[ ]:





# ### Q2) display value 20 from the following tuple
# ### aTuple = ("Orange", [10, 20, 30], (5, 15, 25))

# In[7]:


aTuple = ("Orange", [10, 20, 30], (5, 15, 25))
print(aTuple[1][1])


# In[ ]:





# ### Q3) Unpack the following tuple into 4 variables
# ### aTuple = (10, 20, 30, 40)

# In[10]:


aTuple = (10, 20, 30, 40)

var1, var2, var3, var4 = aTuple

print(var1, var2, var3, var4)


# In[ ]:





# ### Q4) Swap the following two tuples
# 
# tuple1 = (11, 22)
# 
# tuple2 = (99, 88)

# In[11]:


tuple1 = (11, 22)
tuple2 = (99, 88)

temp_tuple = tuple1
tuple1 = tuple2

tuple2 = temp_tuple

print(f"tuple1: {tuple1}")
print(f"tuple2: {tuple2}")


# In[ ]:





# ### Q5) Copy element 44 and 55 from the following tuple into a new tuple
# 
# tuple1 = (11, 22, 33, 44, 55, 66)
# 
# Expected output:
# 
# tuple2: (44, 55)

# In[13]:


tuple1 = (11, 22, 33, 44, 55, 66)

tuple2 = tuple1[3:5]  

print(f"tuple2: {tuple2}")


# In[ ]:





# ### Q6) Modify the first item (22) of a list inside a following tuple to 200
# 
# tuple1 = (11, [22, 33], 44, 55)

# In[1]:


tuple1 = (11, [22, 33], 44, 55)
tuple1[1][0]=200
print(tuple1)


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




