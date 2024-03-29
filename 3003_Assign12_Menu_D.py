#!/usr/bin/env python
# coding: utf-8

# ### Q1) Write a menu driven program to practice String functions
# Design following menu
# 
# a. display characters from even position
# 
# b. display characters from odd position
# 
# c. display length of a string
# 
# d. add a at the end of string length times
# 
# e. exit

# In[1]:


import sys
choice=0

def stringinput():
    return input("enter the string\n")

def evenposition():
    str1=stringinput()
    #for a,b in enumerate([*str1]):
    #  if(a+1)%2==0:
    #    print(b)
    return str1[1::2]

def oddposition():
    str1=stringinput()
    return str1[0::2]

def lenstr():
    str1=stringinput()
    return len(str1)

def add():
    str1=stringinput()
    return str1+"a"*len(str1)



while choice!=5:
    choice=int(input("""
    1)display characters from even position
    2)display characters from odd position
    3)display length of a string
    4)add at the end of string
    5)exit\n"""))
    match choice:
        case 1:
            print(evenposition())
            
        case 2:
            print(oddposition())
            
        case 3:
            print(lenstr())
        case 4:
            print(add())
        case 5:
            print("thank you for visiting........!")
            sys.exit()
        case _:
            print("Invalid input...")


# In[ ]:





# ### Q2) Write a program to accept a string from user. 
# Accept a second string from user to search and find all occurrences of in the given string.
# e.g 
# 
# s1=This is string
# 
# check=is;
# is-;
# is-;
# count=2.
# 
# s1=”this is cat and cat is cute, where is your cat?”
# 
# check=cat;
# cat-8;
# cat-16;
# cat-43;
# count=3;

# In[2]:


str1=input("Enter the string:")
str2=input("Enter the substring :")
count=0
start=0
while True:
  t=str1.find(str2,start)
  if t!=-1:
    print(f"{str2} : {t}")
    count+=1
    start=t+1
  else:
    break
print("count",count)


# ### Q3) Write a menu driven program to practice List functions. Validate input data wherever required.
# Display following menu:
# 
# 1. Accept Data
# a) add at last position
# b) add at given position
# 
# 2. Delete data by value
# display message deleted successfully 
# or not found
# 
# 3. delete data by position
# a) delete last element
# b) delete from particular position
# 
# 4. sort 
# a) ascending 
# b) descending
# 
# 5. reverse
# 
# 6. Print in sorted order without changing original list
# 
# 7. print in reverse order without changing original list
# 
# 8. display data
# a) normal 
# b) numbered

# In[15]:


import sys
list1=[1,2,3,4,5,6,7,8]

def accept_data(value,pos=None):
    if pos:
        list1[pos]=value
        return 1
    else:
        list1.append(value)
        return 2
def display_data():
    return list1

def delete_by_value(value,lst):
    if value in lst:
        lst.remove(value)
        return 1
    else:
        return 2

def delete_by_position(pos,list1):
    if pos<=(len(list1)-1):
        list1.pop(pos)
        return 1
    else:
        return 2
    
def sort1(list1,order=True):
    if order:
        sorted(list1,reverse=order)
        return 1
    else:
        sorted(list1,reverse=not order)
        return 2
    
def reverse(list1):
    return list1[::-1]

def sorted_without_changing_original_list(list1, order):
    list_copy=list1.copy()
    print(sorted(list_copy,reverse=order))

def reverse_list_without_changing_original_list(list1):
    list_copy=list1.copy()
    return list_copy[::-1]


choice=0
while choice!=8:
    choice=int(input("""
    
    1.Accept Data
    2.Delete data by value
    3.Delete data by position
    4.Sort
    5.Reverse
    6.Print in sorted order without changing original list
    7.Print in reverse order without changing original list
    8.Display data
    9.End"""))
    
    match choice:
        case 1:
            n=input("Do you want to update value at last y/n")
            if n=="y":
                value=input("Enter the value")
                T=accept_data(value,pos=None)
                if T==2:
                    print("The value added at the end of list")
                elif n=="n":
                    value=input("Enter the value")
                    pos=input("Enter the position:")
                    T=accept_data(value,pos=int(pos))
                    if T==1:
                        print(f"The value added at pos:{pos}")
                    else:
                        print("Invalid input")
        case 2:
            val=input("Enter the value:")
            res=delete_by_value(val,list1)
            if res==1:
                print("Value found and deleted successfully")
            else:
                print("Value is not found.....")
        case 3:
            pos=int(input("Enter the position"))
            res=delete_by_position(pos,list1)
            if res==1:
                print("Data deleted successfully")
            else:
                print("Position is not found")
        case 4:
            res=sort1(list1,order=True)
            if res==1:
                print("sorted in ascending order:", list1)
            else:
                print("sorted in descending order", list1)
        case 5:
            res=reverse(list1)
            print(res)
        case 6:
            order=int(input("ascending order==0 descending==1"))
            print(sorted_without_changing_original_list(list1, order))
        case 7:
            res=reverse_list_without_changing_original_list(list1)
            print(res)
        case 8:
            print(display_data())
        case 9:
            print("Thank you for visit...........!")
            sys.exit()
        case _:
            print("Invalid input....")


# In[ ]:





# ### Q4) Create two lists to store cities and locations by accepting values from user. 
# 
# Display 1st city and 1st location
# 
# then 2nd city and 2nd location .

# In[3]:


num_entries = int(input("Enter the number of cities and locations: "))

cities = []
locations = []

for i in range(num_entries):
    city = input(f"Enter city {i + 1}: ")
    location = input(f"Enter location for {city}: ")
    cities.append(city)
    locations.append(location)

for city, location in zip(cities, locations):
    print(f"{location} is located in {city}")


# ### Q5)Create a list and exchange the values as index and index as values.
# 
# lst=[12, 1, 3, 7, 8, 5, 8]
#  
# 

# In[3]:


import math
lst=[12, 1, 3, 7, 8, 5, 8]
lst2=[-1 for i in range(max(lst)+1)]
for i in lst:
  lst2[i]=lst.index(i)
print(lst2)


# In[ ]:





# ### Q6) Write a menu driven program to practice Set functions. 
# Write a program to accept names from users and store it in a set.
# 
# Display the following menu:
# 
# print("""1. delete element if exists otherwise do not show any errr""")
# 
# print("2. add a elemet")
# 
# print("3. create one more set")
# 
# print("4. union of 2 sets")
# 
# print("4. intersection of 2 sets")
# 
# print("5. difference of 2 sets")
# 
# print("6. convert set into frozenset")
# 
# print("6. exit") 

# In[ ]:


set1=set()
set2=set()
n=int(input("how many number you want to add in set ?"))
for i in range(n):
    e1=int(input("enter set elements"))
    set1.add(e1)
    print(set1)
        

def deletem(set1):
    e=int(input("enter the element"))
    set1.remove(e)
    print(set1)
    
def addelemt(set1):
    e=int(input("enter the element"))
    set1.add(e)
    print(set1)

def createset():
   
    n=int(input("how many number you want to add in set ?"))
    for i in range(n):
        e2=int(input("enter set elements"))
        set2.add(e2)
        print(set2)
#     set2=set((input("enter the element").split()))
#     print(set2)
    
def  unionofset(set1,set2):
    u=set1|set2
    print(u)

def Intersection(set1,set2):
    inters=set1 & set2
    print(inters)

def difference(set1,set2):
    d=set1-set2
    print(d)
def frozen(set1):
    s=frozenset(set1)
    print(s)
    
def displayall():
    print(set1)
    print(set2)
    
    
choice=0
while choice!=10:
    choice=int(input('''1. delete element if exists otherwise
do not show any errr
2. add a elemet
3. create one more set
4. union of 2 sets
5. intersection of 2 sets
6. difference of 2 sets
7. convert set into frozenset
8.display all
9. exit
    
    '''))
    
    match choice:
        case 1:
            deletem(set1)
        case 2:
            addelemt(set1)
        case 3:
            createset()
        case 4:
            unionofset(set1,set2)
        case 5:
            Intersection(set1,set2)
        case 6:
            difference(set1,set2)
        case 7:
            frozen(set1)
        case 8:
            displayall()
        case 8:
            exit
        case _:
            print("invalid case")


# In[ ]:





# ### Q7) Generate a list of lists (NOTE: List should get generated dynamically)
# Accept a number from user and check last digit of the number.
# 
# If it is 1 then add it in the list at 1st position.
# 
# If 0 then it should get added at list in 0th position.
# 
# e.g list should look as follows
# 
# [[10],[51],[52]]
# 
# [[10,30,20,40],[11,31,41,31],[22,32,42]....]
# 
# if user enters 15 then the resultant list should be
# 
# [[10,30,20,40],[11,32,41,31],[22,32,42],[],[],[15]]

# In[ ]:


lst=[[10,30,20,40],[11,31,41,31],[22,32,42]]


while True:
    num=int(input("Enter the number"))
    e=num % 10
    if  e < len(lst):
        for e in lst:
            num=lst[e]
    print(lst)


# In[ ]:





# ### Q8)Create a list to store strings in a list in following manner list 
# [dxz,axz,bat,rat,cat,pat,bbc,bbm,cbm,....] pat axz
# 
# All list with same character at second position should be consecutive.
# 
# If user adds sat, then the resultant list will be:
# 
# [bat,rat,cat,sat,bbc,bbm,cbm,....]
# 
# If user adds pick, then it should be added at 
# 
# [bat,rat,cat,bbc,bbm,cbm,pick]

# In[1]:


from collections import defaultdict

def create_sorted_list():
  char_groups = defaultdict(list)  # Use defaultdict for efficient grouping
  result = []

  for word in ["dxz", "axz", "bat", "rat", "cat", "pat", "bbc", "bbm", "cbm"]:
    char_groups[word[1]].append(word) 

  for char, words in char_groups.items():
    words.sort()
    result.extend(words)

  return result

sorted_list = create_sorted_list()

sorted_list.append("sat")
sorted_list.append("pick")

print(sorted_list)


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





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




