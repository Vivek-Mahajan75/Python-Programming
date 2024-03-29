#!/usr/bin/env python
# coding: utf-8

# ### Q1) Using numpy create a matrix of size 3 by 5. Create another matrix of 5 by 3 Perform following operations on the matrices
# 1. Display shape of both matrix
# 2. Find matrix multiplication
# 3. Create another matrix of size 3 by 5 using random numbers
# 4. And display addition subtraction and member wise multiplication 
# 
# 1. accept numbers from user and store it in a list1 and list2 then convert these list into ndarray create list3 and list4 to store numbers and convert it into ndarray
# 
# (list1 and list 2 in one array)
# 
# (list3 and list 4 in another array)
# 
# combine these 4 arrays into 2D arrays (use stack functions) and find memberwise addition,multiplication and exponential of first array

# In[1]:


import numpy as np
matrix_a=np.arange(9)
matrix_a=np.resize(matrix_a,(3,3))
matrix_b=np.arange(15)
matrix_b=np.resize(matrix_b,(5,3))
print(matrix_b.shape)
print(matrix_a.shape)


# In[2]:


np.matmul(matrix_b,matrix_a)


# In[3]:


matrix_d = np.random.rand(3, 5)
matrix_d


# In[4]:


matrix_d+np.resize(matrix_b,(3,5))


# In[5]:


matrix_d-np.resize(matrix_b,(3,5))


# In[6]:


list1 = []
list2 = []
n = int(input("Enter the number of elements: "))
for i in range(0, n):
    ele = int(input("Enter element " + str(i + 1) + " for list 1: "))
    list1.append(ele)
for i in range(0, n):
    ele = int(input("Enter element " + str(i + 1) + " for list 2: "))
    list2.append(ele)

# Convert the lists to numpy arrays
array1 = np.array(list1)
array2 = np.array(list2)


# In[7]:


array1,array2


# In[ ]:





# ### Q2) Store yearwise sales of 2 dealers for tv, freeze, mobiles, washing machines, AC and dishwashers for years (2001 to 2010)
# DEALER1
# 
# tv freeze mobiles washing machines AC dishwashers 
# (2001) 0 10000 2000 30000 4000 2000 3000
# (2002) 1 10000 2000 30000 4000 2000 3000 
# 
# Answer the following
# a. Find total yearwise sales of tv,freeze,mobile,….. product for both dealer.
# 
# b. Find in each year total how many products are sold by dealer1 and how many 
# products are sold by dealer 2.
# 
# c. Display average sales of a 2005 year for each dealer.
# 
# d. Display max sales of a 2005 year for each dealer.
# 
# e. Display sales of TV and freeze for each dealer.
# 
# f. Draw 2 bar chart one for each dealer, for each year total number of items sold in the 
# year
# 
# g. Draw a pie chart one for each dealer, for each year total number of items sold in the

# In[1]:


import matplotlib.pyplot as plt

# Dealer 1 data
dealer1_data = {
    2001: {'TV': 0, 'Freeze': 10000, 'Mobiles': 2000, 'Washing Machines': 30000, 'AC': 4000, 'Dishwashers': 2000},
    2002: {'TV': 1, 'Freeze': 10000, 'Mobiles': 2000, 'Washing Machines': 30000, 'AC': 4000, 'Dishwashers': 2000}
}

# Dealer 2 data
dealer2_data = {
    2001: {'TV': 0, 'Freeze': 12000, 'Mobiles': 2500, 'Washing Machines': 35000, 'AC': 4500, 'Dishwashers': 2500},
    2002: {'TV': 2, 'Freeze': 12000, 'Mobiles': 2500, 'Washing Machines': 35000, 'AC': 4500, 'Dishwashers': 2500}
}

# a. Total yearwise sales for both dealers
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

# b. Total products sold by each dealer per year
def total_products_sold_by_dealer(dealer_data):
    total_products_sold = {}
    for year, products in dealer_data.items():
        total_products_sold[year] = sum(products.values())
    return total_products_sold

dealer1_products_sold = total_products_sold_by_dealer(dealer1_data)
dealer2_products_sold = total_products_sold_by_dealer(dealer2_data)
print("Dealer 1 Products Sold:", dealer1_products_sold)
print("Dealer 2 Products Sold:", dealer2_products_sold)

# c. Average sales for 2005
# d. Max sales for 2005 - Not provided in the given data

# e. Sales of TV and Freeze for each dealer
print("Sales of TV and Freeze for Dealer 1:", dealer1_data[2001]['TV'], dealer1_data[2001]['Freeze'])
print("Sales of TV and Freeze for Dealer 2:", dealer2_data[2001]['TV'], dealer2_data[2001]['Freeze'])

# f. Draw bar charts
def draw_bar_chart(data, title):
    plt.bar(data.keys(), data.values())
    plt.title(title)
    plt.xlabel('Year')
    plt.ylabel('Total Items Sold')
    plt.show()

draw_bar_chart(dealer1_products_sold, 'Dealer 1 Total Items Sold per Year')
draw_bar_chart(dealer2_products_sold, 'Dealer 2 Total Items Sold per Year')

# g. Draw pie charts
def draw_pie_chart(data, title):
    plt.pie(data.values(), labels=data.keys(), autopct='%1.1f%%', startangle=140)
    plt.title(title)
    plt.axis('equal')
    plt.show()

draw_pie_chart(dealer1_products_sold, 'Dealer 1 Total Items Sold per Year')
draw_pie_chart(dealer2_products_sold, 'Dealer 2 Total Items Sold per Year')


# In[ ]:


choice = 0
while True:
    choice = int(input("""
      1. View Products
      2. Add a Product
      3. Exit
      """))
    match choice:
      case 1:
          # Code to view products
          print("Viewing products...")
      case 2:
          # Code to add a product
          print("Adding a product...")
      case 3:
          print("Exiting program...")
          exit(0)  # Exit the program gracefully
      case _:
          print("Invalid choice. Please try again.")


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




