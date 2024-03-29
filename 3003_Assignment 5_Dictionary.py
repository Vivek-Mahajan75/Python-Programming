#!/usr/bin/env python
# coding: utf-8

# ### Q1) the two lists convert it into the dictionary
# keys = ['Ten', 'Twenty', 'Thirty']
# 
# values = [10, 20, 30]

# In[9]:


keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

my_dict = {}

for i in range(len(keys)):

      my_dict[keys[i]] = values[i]

print(my_dict)


# In[ ]:





# ### Q2)Merge following two Python dictionaries into one
# dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
# dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

# In[1]:


dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}

dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

dict3 = {**dict1, **dict2}

print(dict3)


# In[ ]:





# ### Q3)Display the value of key history from the following dictionary
# the value of key ‘history’ from the below dict
# 
# sampleDict = { 
# 
#  "class":{ 
#  
#  "student":{ 
#  
#  "name":"Mike",
#  
#  "marks":{ 
#  
#  "physics":70,
#  
#  "history":80
#  }
#  }
#  }

# In[16]:


sampleDict = {"class": {"student": {"name": "Mike","marks": {"physics": 70,"history": 80}}}}

history_score = sampleDict["class"]["student"]["marks"]["history"]

print(history_score)


# In[ ]:





# ### Q4)Delete set of keys from a dictionary
# Given:
# sampleDict = {
#  "name": "Kelly",
#  "age":25,
#  "salary": 8000,
#  "city": "New york" 
# }

# In[15]:


sampleDict = { "name": "Kelly", "age":25, "salary": 8000, "city": "New york" }

del sampleDict["name"]
del sampleDict["salary"]

print(sampleDict)


# ### Q5) display all the keys with value 200 from the following dictionary.
# sampleDict = {'a': 100, 'b': 200, 'c': 300,’d’:200}

# In[6]:


sampleDict = {'a': 100, 'b': 200, 'c': 300, 'd': 200}

for key, value in sampleDict.items():
      if value == 200:
print(key)


# In[ ]:





# ### Q6) Rename key city to location in the following dictionary
# sampleDict = {"name": "Kelly", "age":25, "salary": 8000, "city": "New york"}

# In[7]:


sampleDict = { "name": "Kelly", "age":25, "salary": 8000, "city": "New york" }

sampleDict["location"] = sampleDict.pop("city")

print(sampleDict)  


# In[ ]:





# ### Q7) display the key of a maximum value from the following dictionary
# sampleDict = {'Physics': 82 ,'Math': 65 ,'history': 75}

# In[8]:


sampleDict = {'Physics': 82,'Math': 65,'history': 75 }

max_key=max(sampleDict,key=sampleDict.get)
print("the key with maximum value is:",max_key)


# In[ ]:





# ### Q8) Accept name and new salary for a employee, modify salary of the employee. display 
# ### appropriate message if salary modified. or if name not found.
# note : the new salary should be > current salary otherwise show message wrong salary.
# 
# sampleDict = {
# 
#  'emp1': {'name': 'Jhon', 'salary': 7500},
#  
#  'emp2': {'name': 'Emma', 'salary': 8000},
#  
#  'emp3': {'name': 'Brad', 'salary': 6500}
#  }
# 

# In[1]:


def modify_salary(emp_dict, emp_name, new_salary):
    employee = None
    for key, value in emp_dict.items():
        if value['name'] == emp_name:
            employee = value
            break
    
    if employee:
        if new_salary > employee['salary']:
            employee['salary'] = new_salary
            return f"Salary for {emp_name} updated to {new_salary}."
        else:
            return "New salary must be higher than current salary."
    else:
        return f"Employee '{emp_name}' not found."

sampleDict = {
    'emp1': {'name': 'Jhon', 'salary': 7500},
    'emp2': {'name': 'Emma', 'salary': 8000},
    'emp3': {'name': 'Brad', 'salary': 6500}
}

employee_name = input("Enter employee name: ")
new_salary = int(input("Enter new salary: "))

message = modify_salary(sampleDict, employee_name, new_salary)
print(message)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




