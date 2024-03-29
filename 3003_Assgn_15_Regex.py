#!/usr/bin/env python
# coding: utf-8

# ### Q1) Do the following using Regular Expression:
# 1. accept lines from user and store in a list.
# 
# convert list into dictionary as follows
# 
# {
# 
#  “found”:[“this is algorithm”, “this is mid”],
#  
# “not found:[“this is data”,”this is min”]
# 
# }

# In[13]:


import re

lines = []
while True:
    line = input("Enter a line (or type 'done' to finish): ")
    if line.lower() == 'done':
        break
    lines.append(line)

pattern = re.compile(r'\bthis is (algorithm|mid)\b')

result = {"found": [], "not found": []}

for line in lines:
    if pattern.search(line):
        result["found"].append(line)
    else:
        result["not found"].append(line)
print(result)


# In[ ]:





# ### Q2) accept strings in following format from user and store it in a list: 
# 12, queen,2018, kangana, 1234562018, pune 
# 
# 15, dangal,2018, aamir, 34562562018, mumbai 
# 
# 12, sholay,1995, amitabh, 7869272018, pune 
# 
#  ---- Display movie name and year separated by, if the movie was released in 2018.
#  
#  ---- Display movies released in pune city.

# In[7]:


movies_data = [
    "12, queen,2018, kangana, 1234562018, pune",
    "15, dangal,2018, aamir, 34562562018, mumbai",
    "12, sholay,1995, amitabh, 7869272018, pune"
]

# Display movie name and year separated by ',' if released in 2018
print("Movies released in 2018:")
for movie_info in movies_data:
    info = movie_info.split(',')
    if info[2].strip() == '2018':
        print(f"{info[1]}, {info[2]}")

# Display movies released in pune city
print("\nMovies released in Pune:")
for movie_info in movies_data:
    info = movie_info.split(',')
    if info[-1].strip() == 'pune':
        print(info[1])


# In[ ]:





# ### Q3) Accept 2 patterns from user
# 
# Accept multiple strings from user till user enters end, if string has pattern 1 then store it in list1
# 
# If it has pattern 2 then store it in list2 else display message pattern not found

# In[6]:


list1 = []
list2 = []

pattern1 = input("Enter pattern 1: ")
pattern2 = input("Enter pattern 2: ")

while True:
    string = input("Enter a string (or 'end' to stop): ")
    if string == 'end':
        break

    if pattern1 in string:
        list1.append(string)
    elif pattern2 in string:
        list2.append(string)
    else:
        print("Pattern not found")

print("\nStrings with pattern 1:", list1)
print("Strings with pattern 2:", list2)


# In[ ]:





# In[ ]:




