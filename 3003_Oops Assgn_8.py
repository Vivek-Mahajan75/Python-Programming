#!/usr/bin/env python
# coding: utf-8

# ### Q1) Write a program to maintain student information. For each student store studid, name, m1, 
# ### m2 and m3 (marks of 3 subjects ). Accept information for 2 students and display it as follows.
# Student Details:
# 
# Student Id
# 
# Name: Divya
#  
# M1 : 78
# 
# M2: 86
# 
# M3: 89

# In[1]:


students = []
for i in range(2):  
    student_id = int(input("Enter student ID: "))
    name = input("Enter student name: ")
    m1 = int(input("Enter marks for M1: "))
    m2 = int(input("Enter marks for M2: "))
    m3 = int(input("Enter marks for M3: "))

    student = {"studid": student_id, "name": name, "m1": m1, "m2": m2, "m3": m3}
    students.append(student)

print("\nStudent Details:")
print("____________\n")

for student in students:
    print(f"Student Id: {student['studid']}")
    print(f"Name: {student['name']}")
    print(f"M1 : {student['m1']}")
    print(f"M2: {student['m2']}")
    print(f"M3: {student['m3']}\n")

print("End of student information.")


# In[ ]:





# ### Q2) Write a menu driven program to maintain student information. Modify Student class created in previous assignment. Add a member gpa in student class, add a function in student class to return GPA of a student
# calculateGPA()
# 
# gpa=(1/3)*m1+(1/2)*m2+(1/4)*m3
# 
# Create an array to store Multiple students.
# 
# 1. Display All Student
# 
# 2. Search by id
# 
# 3. Search by name
# 
# 4. calculate GPA of a student
# 
# 5. Exit

# In[2]:


import sys
import pandas as pd


class Stud():
  count=10
  lst = []
  def __init__(self,name,m1,m2,m3):
    Stud.count+=1
    self.__name=name
    self.__m1=m1
    self.__m2=m2
    self.__m3=m3

  def calGPA(self):
    Stud.lst.append({"id":Stud.count,"name":self.__name, "m1":self.__m1, "m2":self.__m2, "m3":self.__m3,"GPA":(1/3)*self.__m1+(1/2)*self.__m2+(1/4)*self.__m3})

  def __str__(self):
    return f"studid:{Stud.count}\nName:{self.__name}\nm1:{self.__m1}\nm2:{self.__m2}\nm3:{self.__m3}\n"
for i in range(3):
  name=input("Enter the name :")
  m1=float(input("Enter m1:"))
  m2=float(input("Enter m2:"))
  m3=float(input("Enter m2:"))
  p=Stud(name,m1,m2,m3)
  p.calGPA()
choice=0
while True:
  choice=int(input("""
  1) Display All Student
  2) Search by id
  3) Search by name
  4) calculate GPA of a student
  5) Exit
  """))
  match choice:
    case 1:
      studinfo=pd.DataFrame(p.lst)
      print(studinfo)
      # for item in p.lst:
      #   print(f"Id: {item['id']}\nName: {item['name']}\nSubject 1: {item['m1']}\nSubject 2: {item['m2']}\nSubject 3: {item['m3']}\nGPA: {round(item['GPA'],2)}\n")
    case 2:
      id=int(input("Enter the id :"))
      for dis in p.lst:
        if dis["id"]==id:
          ZSifd=pd.DataFrame(dis,index=[0]).set_index('id')
          print(ZSifd)
          break
      else:
        print("id is not exist")
    case 3:
      name=input("Enter the name :")
      for dis in p.lst:
        if dis["name"]==name:
          ZSifd=pd.DataFrame(dis,index=[0]).set_index('id')
          print(ZSifd)
          break
      else:
        print("name is not exist")
    case 4:
      id=int(input("Enter the id :"))
      for dis in p.lst:
        if dis["id"]==id:
          print(dis['GPA'])
          break
      else:
        print("id  is not exist")
    case 5:
      print("By BY ........!!!!!")
      sys.exit()


# In[ ]:





# ### Q3) Write a python program to store information of your friends
# id,name,lastname,hobbies,mobno,email,bdate,address
# 
# Note:- hobbies- a friend may have multiple hobbies
# 
# Accept all friends details and store it in an array and do the following.
# 1. Display All Friend
# 2. Search by id
# 3. Search by name
# 4. Display all friend with a particular hobby 
# 5. Exit

# In[2]:


import sys
import pandas as pd


class Stud():
  count=10
  lst = []
  def __init__(self,name='',lastname='',hobbies=0,mobno='',email='',bdate='',address=''):
    Stud.count+=1
    self.__name=name
    self.__lastname=lastname
    self.__hobbies=hobbies
    self.__mobno=mobno
    self.__email=email
    self.__bdate=bdate
    self.__address=address

  def info(self):
    Stud.lst.append({"id":Stud.count,"name":self.__name, "lastname":self.__lastname, "email":self.__email,"hobbies":self.__hobbies, "mobno":self.__mobno,'address':self.__address})

  def __str__(self):
    return f"id:{Stud.count},name:{self.__name},lastname:{self.__lastname}, hobbies:{self.__hobbies},mobno:{self.__mobno},email:{self.__eamil},address:{self.__address}"


for i in range(2):
  name=input("Enter the name :")
  lastname=input("Enter lastname:")
  hobbies=input("Enter hobbies in comma spreated").split(",")
  mobno=input("Enter mobno")
  email=input("Enter email")
  bdate=input("Enter bdate")
  address=input("Enter address")
  p=Stud(name=name,lastname=lastname,hobbies=hobbies,mobno= mobno,email=email,bdate=bdate,address=address)
  p.info()

choice=0
while True:
  choice=int(input("""
  1) Display All Student
  2) Search by id
  3) Search by name
  4) Display all friend with a particular hobby
  5) Exit
  """))
  match choice:
    case 1:
      studinfo=pd.DataFrame(p.lst)
      print(studinfo)
      # for item in p.lst:
      #   print(f"Id: {item['id']}\nName: {item['name']}\nSubject 1: {item['m1']}\nSubject 2: {item['m2']}\nSubject 3: {item['m3']}\nGPA: {round(item['GPA'],2)}\n")
    case 2:
      id=int(input("Enter the id :"))
      for dis in p.lst:
        # print(isinstance(dis, dict))
        if dis["id"] == id:
          print(dis)
          break
      else:
        print("id is not exist")
    case 3:
      name=input("Enter the name :")
      for dis in p.lst:
        if dis["name"]==name:
          print(dis)
          break
      else:
        print("name is not exist")
    case 4:
        id=input("Enter the hobby :").strip()
        print(id)
        for swp in p.lst:

          if id in swp['hobbies']:
            print(swp["name"])
    case 5:
      print("By BY ........!!!!!")
      sys.exit()


# In[ ]:





# ### Q4)Design a class hierarchy to maintain information for ABCTel telecom company , company wants to maintain information of customers and vendors.
# For vendors they want to store vendorid, name, email, phone number,list of products they supply
# 
# For customers they want to store custid, name, email, credit class(based on credit history), 
# discounts, plan assigned to customer
# 
# Customer may be Individual or a company
# 
# For individual customer, system should store phone number 
# 
# For a customer of type Company, system should store info about relationship manager, credit line, 
# extensions, list of numbers

# In[14]:


import matplotlib.pyplot as plt
dealer1_data = {
    2001: {'TV': 0, 'Freeze': 10000, 'Mobiles': 2000, 'Washing Machines': 30000, 'AC': 4000, 'Dishwashers': 2000},
    2002: {'TV': 1, 'Freeze': 10000, 'Mobiles': 2000, 'Washing Machines': 30000, 'AC': 4000, 'Dishwashers': 2000}}

dealer2_data = {
    2001: {'TV': 0, 'Freeze': 12000, 'Mobiles': 2500, 'Washing Machines': 35000, 'AC': 4500, 'Dishwashers': 2500},
    2002: {'TV': 2, 'Freeze': 12000, 'Mobiles': 2500, 'Washing Machines': 35000, 'AC': 4500, 'Dishwashers': 2500}}

def total_yearwise_sales(dealer_data):
    total_sales = {}
    for year, products in dealer_data.items():
        for product, sales in products.items():
            total_sales.setdefault(product, 0)
            total_sales[product] += sales
    return total_sales
dealer1_total_sales = total_yearwise_sales(dealer1_data)
dealer2_total_sales = total_yearwise_sales(dealer2_data)
print("Dealer 1 Total Sales:", dealer1_total_sales)
print("Dealer 2 Total Sales:", dealer2_total_sales)

def total_products_sold_by_dealer(dealer_data):
    total_products_sold = {}
    for year, products in dealer_data.items():
        total_products_sold[year] = sum(products.values())
    return total_products_sold
dealer1_products_sold = total_products_sold_by_dealer(dealer1_data)
dealer2_products_sold = total_products_sold_by_dealer(dealer2_data)
print("Dealer 1 Products Sold:", dealer1_products_sold)
print("Dealer 2 Products Sold:", dealer2_products_sold)
print("Sales of TV and Freeze for Dealer 1:", dealer1_data[2001]['TV'], dealer1_data[2001]['Freeze'])
print("Sales of TV and Freeze for Dealer 2:", dealer2_data[2001]['TV'], dealer2_data[2001]['Freeze'])

def draw_bar_chart(data, title):
    plt.bar(data.keys(), data.values())
    plt.title(title)
    plt.xlabel('Year')
    plt.ylabel('Total Items Sold')
    plt.show()

draw_bar_chart(dealer1_products_sold, 'Dealer 1 Total Items Sold per Year')
draw_bar_chart(dealer2_products_sold, 'Dealer 2 Total Items Sold per Year')

def draw_pie_chart(data, title):
    plt.pie(data.values(), labels=data.keys(), autopct='%1.1f%%', startangle=140)
    plt.title(title)
    plt.axis('equal')
    plt.show()

draw_pie_chart(dealer1_products_sold, 'Dealer 1 Total Items Sold per Year')
draw_pie_chart(dealer2_products_sold, 'Dealer 2 Total Items Sold per Year')


# In[ ]:





# In[ ]:




