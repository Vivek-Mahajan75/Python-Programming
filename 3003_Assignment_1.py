#!/usr/bin/env python
# coding: utf-8

# ### Q1) A student will not be allowed to sit in exam if his/her attendence is less than 75%.

# In[12]:


a = int(input("Number of classes held"))
b = int(input("Number of classes attended"))

percentage = (b/a)*100
print(percentage)

if percentage <= 75:
    print("Student are not allowed to sit in exam")
else:
    print("Student are allowed to sit in exam")


# In[ ]:





# ### Q2) Accept amount from user and find the minimum number notes required to get the amount

# In[21]:


amount=int(input("Enter the amount"))
if amount//2000>=0:
    print(f"2000 notes :{amount//2000}")
    amount=amount%2000
if amount//500>=0:
    print(f"500 notes :{amount//500}")
    amount=amount%500
if amount//100>=0:
    print(f"100 notes :{amount//100}")
    amount=amount%100
if amount//50>=0:
    print(f"50 notes :{amount//50}")
    amount=amount%50
if amount//10>=0:
    print(f"10 notes :{amount//10}")
    amount=amount%10
if amount//5>=0:
    print(f"5 notes :{amount//5}")
    amount=amount%5
if amount//2>=0:
    print(f"2 coin :{amount//2}")
    amount=amount%2
if amount//1>=0:
    print(f"1 coin :{amount//1}")
    amount=amount%1


# In[ ]:





# ### Q3) Modify the above question to allow student to sit if he/she has medical cause. Ask 
# ### user if he/she has medical cause or not ( 'Y' or 'N' ) and print accordingly.

# In[14]:


a = int(input("Number of classes held"))
b = int(input("Number of classes attended"))

percentage = (b/a)*100
print(percentage)
y=1
n=0
if percentage <= 75:
    print("Student are not allowed to sit in exam")
    reason=int(input("do you have any medical cause 1/0"))
    if reason == y:
        print("Student are allowed to sit in exam")
    else:
        print("Student are not allowed to sit in exam")
else:
    print("Student are allowed to sit in exam")


# In[ ]:





# ### Q4)  A school has following rules for grading system.

# a. Below 25 - F
# 
# b. 25 to 45 - E
# 
# c. 45 to 50 - D
# 
# d. 50 to 60 - C
# 
# e. 60 to 80 - B
# 
# f. Above 80 - A
# 
# Ask user to enter marks and print the corresponding grade

# In[15]:


a = int(input("Enter the marks"))
if a<25:
    print("Grade is F")
elif a>=25 and a<45:
    print("Grade is E")
elif a>=45 and a<50:
    print("Grade is D")
elif a>=50 and a<60:
    print("Grade is C")
elif a>=60 and a<80:
    print("Grade is B")
else:
    print("Grade is A")


# In[ ]:





# ### Q5. Print the output of following statements
# If
# x = 2,
# y = 5,
# z = 0,
# then find values of the following expressions:
# 
# a. x == 2,
# 
# b. x != 5,
# 
# c. x != 5 && y >= 5,
# 
# d. z != 0 || x == 2,
# 
# e. !(y < 10)

# In[16]:


x = 2
y = 5
z = 0

#a)
if x==2:
    print("T")
else:
    print("F")

#b)    
if x!=5:
    print("T")
else:
    print("F")

#c)    
if x!=5 and y>=5:
    print("T")
else:
    print("F")
    
#d)
if z!=0 or x==2:
    print("T")
else:
    print("F")
    
#e)
if not(y<10):
    print("T")
else:
    print("F")


# In[ ]:





# ### Q6) Accept number from user and check whether it is divisible by 5 and 11
# ### if divisible then display appropriate message.
# 

# In[18]:


a=int(input("Enter the number"))
if a % 5==0:
    print("Number is divisible by 5")
else:
    print("Number is not divisible by 5")

if a % 11==0:
    print("Number is divisible by 11")
else:
    print("Number is not divisible by 11")


# In[ ]:





# ### Q7) Write a program to calculate the electricity bill (accept number of unit from user) 
# according to the following criteria :
# 
#  Unit Price 
#  
# First 100 units no charge
# 
# Next 100 units Rs 5 per unit
# 
# After 200 units Rs 10 per unit
# 
# (For example if input unit is 350 than total bill amount is Rs2000)
# 

# In[1]:


units = int(input("Enter the number of units consumed"))
total_bill = 0
if units<=100:
    total_bill = 0
elif units<=200:
    total_bill = (units - 100) * 5
else:
    total_bill = 100*5 + (units - 200) * 10
print(total_bill)


# In[ ]:





# ### Q8) Write a program to check whether the last digit of a number( entered by user ) is divisible by 
# ### 3 or not.
# 

# In[2]:


a=int(input("Enter the number"))
lg=a%10
if lg/3==0:
    print("last digit is divisible by 3")
else:
    print("last digit is not divisible by 3")


# In[ ]:





# ### Q9) Write a program to check whether an years is leap year or not
# the year is leap if it satisfies following condition
# 
# • It the year is divisible by 100
# 
# o If it is divisible by 100, then it should also be divisible by 400 then it is 
# leap year
# 
# • otherwise, all other years divisible by 4 and not divisible by 100 then it is leap 
# year.

# In[20]:


year = int(input("Enter a year"))

if year % 100==0 and year % 400==0:
    print("It is leap year")
elif ((year % 4==0) and (year % 100!=0)):
    print("It is leap year")  
else:
    print("It is not leap year")


# In[ ]:





# ### Q10) Write a program to accept the price of a bike and display the road tax and 
# ### insurance to be paid according to the following criteria . also display total amount to 
# ### be paid.
#  
#  Cost price (in Rs) Tax Inssurance
#  
#  > 100000 15 % 20%
#  
#  > 50000 and <= 100000 10% 8%
#  
#  <= 50000 5% 5%

# In[28]:


price = int(input("Enter the price"))
if price > 100000:
    price = price + ((15/100)*price) + ((20/100)*price)
elif price > 50000 and price <= 100000:
    price = price + ((10/100)*price) + ((8/100)*price)
else: 
    price <= 50000
    price = price + ((5/100)*price) + ((5/100)*price)
print(price)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




