#!/usr/bin/env python
# coding: utf-8

# ### Q1)write a regex to get only the part of the email before the "@" sign excluding the "@" sign.
# example myemail@google.com o/p myemail

# In[2]:


import re
def get_username():
    email = input("Enter an email address: ")
    match = re.search(r"^(.*?)@", email)  
    if match:
        username = match.group(1)  
        print("Username:", username)
    else:
        print("Invalid email address.")

if __name__ == "__main__":
    get_username()


# In[ ]:





# ### Q2) Accept lines from user and display only the lines that start with a number or any 2 alphabets

# In[4]:


import re
line=input("Enter the line:")
pattern=re.search(r"(^\d|.a.b)",line)
if pattern:
    print(line)
else:
    print("Line does not start with a number or any 2 alphabets")


# In[ ]:





# ### Q3) Write a python program to accept mobile number and validate it. it should contain exactly 10 digits. 

# In[2]:


import re
def validate_mobile():
    while True:
        mobile_number = input("Enter mobile number (or 'q' to quit): ")
        if mobile_number.lower() == 'q':
            break

        if re.match(r"\d{10}", mobile_number):  
            print("Valid mobile number!")
            break
        else:
            print("Invalid mobile number. Please enter 10 digits only.")

if __name__ == "__main__":
    validate_mobile()


# In[ ]:





# ### Q4) Write a python program to accept user name and password and validate it. 
# username should contain only alphabets or digits and password length should be 8, starts with 
# 
# alphabet and should contain at least one special character(#,@).
# 
# accept username and password from user and validate it. if it is valid then display message 
# 
# welcome to our application. otherwise ask to re-enter.
# 
# (allows maximum 3 attempts to accept password

# In[5]:


import re
def validate_username(username):
    return username.isalnum()

def validate_password(password):
    pattern = "^(?=.*[a-zA-Z])(?=.*[#@]).{8,}$"

    return bool(re.match(pattern, password))

def login():
    attempts = 3
    while attempts > 0:
        username = input("Enter username: ")
        password = input("Enter password: ")

        if validate_username(username) and validate_password(password):
            print("Welcome to our application!")
            break
        else:
            attempts -= 1
            print("Invalid username or password. Please try again.")
            if attempts == 0:
                print("Maximum attempts reached. Login failed.")

if __name__ == "__main__":
    login()


# In[ ]:




