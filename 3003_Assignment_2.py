#!/usr/bin/env python
# coding: utf-8

# ### Q1) Accept 10 integers from user and print their average value on the screen

# In[1]:


total = 0
count = 0

for i in range(10):
  number = int(input("Enter number " + str(i+1) + ": "))
  total += number
  count += 1

if count > 0:  
  average = total / count
  print("The average of the entered numbers is:", average)
else:
  print("No numbers were entered.")


# In[ ]:





# ### Q2. Print the following patterns using loop :
# 
# a.
# *
# **
# ***
# ****
# 
# b.
#   *
#  ***
# *****
# ***
#  *
#  
# c.
# 1010101
# 10101
# 101
# 1
# 
# d.
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

# In[38]:


#a
for i in range(1,6):
    for j in range(1,i):
        print("*",end=" ")
    print()
    
    
#b
for i in range(3):
    print(" "*(3-i),"*"*(i*2+1))
for i in range(3-2,-1,-1):
    print(" "*(3-i),"*"*(i*2+1))
    
    
#c
for i in range(4,-1,-1):
    print(" "*(4-i),"10"*i)
        
    
#d  
for i in range(1,6):
    for j in range(1,i):
        print(j,end=" ")
    print()


# In[ ]:





# ### Q3) Write a program to find greatest common divisor (GCD) or highest common factor (HCF) of 
# ### given two numbers.
# 

# In[39]:


num1=int(input("enter first number:"))
num2=int(input("enter second number:"))

if num2>num1:
    min=num1
else:
    min=num2
                                      
for i in range(1,min+1):
    if num1 % i == 0 and num2 % i==0:
        hcf=i
print("HCF/GCD of these two numbers is{hcf}:",hcf)


# In[ ]:





# ### Q4) Take integer inputs from user until he/she presses q ( Ask to press q to quit after every 
# ### integer input ). Print average and product of all numbers.

# In[41]:


q=""
sum1=0
product=1
count=0
while q !="q":
    q= input("Enter an integer (press 'q' to quit):")
    if q!="q":
        sum1+=int(q)
        product*=int(q)
        count+=1
print(f"Average is:{sum1/count}\nProduct is :{product}")


# In[ ]:





# ### Q5)Given a number count the total number of digits in a number and also find sum of digits of 
# ### the number.
# 

# In[42]:


n=12345
sum1 = 0
count=0
while n!= 0:
    sum1+=n%10
    count+=1
    n//=10
print(f"Sum:{sum1}\nCount:{count}")


# ### Q6) To display the cube of the number upto given an integer. If the given integer is 5, then 
# ### display cube of 1 to 4.

# In[44]:


num = int(input("Enter an integer:"))
for i in range(1,num):
    print(i**3)


# In[ ]:





# ### Q7) Accept 20 numbers from user and display sum of only even numbers.

# In[45]:


total = 0

for i in range(20):
    num = int(input("Enter a number:"))
    if num%2 == 0:
        total+=num
        
print(f"Sum of all the even numbers is {total}")


# ###### 

# In[ ]:





# ### Q8) Ask user number of terms to be generated of a series.
# ### generate numbers for the following series and find its addition
# [9 + 99 + 999 + 9999+……..]

# In[46]:


n = int(input("Enter the term"))
temp = 9
sum = 0
for i in range(1,n,1):
    sum = sum+temp
    print(temp)
    temp = temp*10+9
print("the sum of series :",sum)


# In[ ]:





# ### Q9) Write a program in python to display the sum of the series [ 1+x+x^2/2!+x^3/3!+....]. Go to 
# ### the editor
# 
# Test Data :
# 
# Input the value of x :3
# 
# Input number of terms : 5
# 
# Expected Output :
# 
# The sum is : 16.375000
# 

# In[47]:


import math
x=3
sum=1
n=5
for i in range(1,n,1):  
    sum=sum + (pow(x,i)/math.factorial(i))     
print(sum)


# In[ ]:





# ### Q10) Write a program in python to find the sum of the series [ x - x^3 + x^5 + ......]. Go to the editor
# Test Data :
# 
# Input the value of x :2
# 
# Input number of terms : 5
# 
# Expected Output :
# 
# The values of the series:
# 
# 2,
# -8,
# 32,
# -128,
# 512.
# 
# The sum = 410

# In[1]:


x = int(input("Enter the value of x: "))
num_terms = int(input("Enter number of terms: "))

series = [(-1)**i * x**(2*i + 1) for i in range(num_terms)]

series_sum = sum(series)

print("The values of the series:", series)
print("The sum =", series_sum)


# 

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




