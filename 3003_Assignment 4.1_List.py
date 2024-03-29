#!/usr/bin/env python
# coding: utf-8

# ### Q1) Reverse a given list in Python
# aLsit = [100, 200, 300, 400, 500]
# 

# In[1]:


aLsit = [100, 200, 300, 400, 500]
aLsit.reverse()
print(aLsit)


# In[ ]:





# ### Q2) Concatenate two lists index-wise
# Given:
# 
# list1 = ["M", "na", "i", "Raj"]
# 
# list2 = ["y", "me", "s", "esh"]

# In[ ]:





# In[3]:


list1 = ["M", "na", "i", "Raj"]

list2 = ["y", "me", "s", "esh"]

concatenate_list = [a+b for a,b in zip(list1,list2)]
print(concatenate_list)


# In[ ]:





# ###  Q3) Given a Python list of numbers. Turn every item of a list into its square
# aList = [1, 2, 3, 4, 5, 6, 7]

# In[5]:


aList = [1, 2, 3, 4, 5, 6, 7]

squared_list = [num ** 2 for num in aList]

print(squared_list)


# In[ ]:





# ###  Q4) Concatenate two lists in the following order
# 
# list1 = ["Hello ", "Welcome "]
# 
# list2 = ["Students", "Sir"]

# In[22]:


list1 = ["Hello ", "Welcome "]
list2 = ["Students", "Sir"]
list3 = []
for i in range(len(list1)):
    for j in range(len(list2)):
        list3.append(list1[i] + list2[j])
print(list3)


# In[ ]:





# ### Q5) Given a two Python list. Iterate both lists simultaneously such that list1 should display item 
# in original order and list2 in reverse order
# 
# list1 = [10, 20, 30, 40]
# 
# list2 = [100, 200, 300, 400]
# 

# In[1]:


list1 = [10, 20, 30, 40]

list2 = [100, 200, 300, 400]

for i in range(len(min(list1, list2))):
  print(f"{list1[i]}  {list2[::-1][i]}")


# In[ ]:





# ### Q6 Remove empty strings from the list of strings
# list1 = ["Ashish", "", "Atharva", "Amit", "", "Revati"]

# In[1]:


list1 = ["Ashish", "", "Atharva", "Amit", "", "Revati"]

i = 0
while i < len(list1):
    if list1[i] == "":
        list1.remove("")
    else:
        i += 1
print(list1)


# In[ ]:





# ### Q7) Add item 7000 after 6000 in the following Python List
# list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]

# In[2]:


list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]

list1[2][2].insert(list1[2][2].index(6000) + 1, 7000)

print(list1)


# In[ ]:





# ### Q8) Given a nested list extend it by adding the sub list ["h", "i", "j"] in such a way that it will look 
# like the following list
# 
# list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
# 
# Sub List to be added = ["h", "i", "j"]

# In[3]:


list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]

subList = ["h", "i", "j"]

list1[2][1][2].extend(subList)

print(list1)


# In[ ]:





# ### Q9) Given a Python list, find value 20 in the list, and if it is present, replace it with 200. Only 
# update the first occurrence of a value
# 
# list1 = [5, 10, 15, 20, 25, 50, 20]

# In[6]:


list1 = [5, 10, 15, 20, 25, 50, 20]

for i in range(len(list1)):

  if list1[i] == 20 :

    list1[i] = 200
    break 

print(list1)


# In[ ]:





# ### Q10) Given a Python list, remove all occurrence of 20 from the list
# list1 = [5, 20, 15, 20, 25, 50, 20]

# In[7]:


list1 = [5, 20, 15, 20, 25, 50, 20]

output = [x for x in list1 if x != 20]

print(output) 


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




