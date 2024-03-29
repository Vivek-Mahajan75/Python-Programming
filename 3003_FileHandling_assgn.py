#!/usr/bin/env python
# coding: utf-8

# ### Q1)Write a python program to accept mobile number and validate it. it should contain exactly 10 digits. 
# (use regularexpression---→ \d{10} -- it will match 10 digit number

# In[4]:


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





# ### Q2) Create a file productdata.txt, using notepad and add contents in following format
# Id:name:description:category:price
# 
# For example
# 123:lays:very crispy:chips:40
# 124:Good day:very sweet:biscuits:35
# 125:maggi:yummy:snacks:60
# 225:chings:yummy:snacks:65
# 123:nachos:very crispy:chips:120
# 
# a. Write a python program read data from file productdata.txt, copy all the lines starting with 12 
# and ending with 0 in file myproduct.txt
# 
# (use regular expression ^12.*0$)
# 
# b. Write a python program to find sum of prices for each category
# 
# Example the o/p should be as follows
# Chips-→160
# Biscuits-→35
# Snacks-→125
# (hint : use dictionary)
# 
# c. Write a python program to accept category from user, display all products of the given category
# Example 
# 
# if category given is chips then use regular expression :chips:
# 
# if category given is chips then use regular expression :snack:
# 
# generate patter :<givencategory name>: and use it for finding lines of the given category

# In[2]:


import re

def read_product_data(filename):

  products = []
  with open(filename, "r") as file:
    for line in file:

      data = line.strip().split(":")
      if len(data) == 5: 
        product = {
            "id": data[0],
            "name": data[1],
            "description": data[2],
            "category": data[3],
            "price": int(data[4])  
        }
        products.append(product)
  return products

def copy_specific_lines(data, pattern, output_filename):

  with open(output_filename, "w") as outfile:
    for product in data:
      line = f"{product['id']}:{product['name']}:{product['description']}:{product['category']}:{product['price']}\n" 
      if re.match(pattern, line): 
        outfile.write(line)

def calculate_price_sum_by_category(data):

  category_prices = {}
  for product in data:
    category = product["category"]
    price = product["price"]
    if category not in category_prices:
      category_prices[category] = 0
    category_prices[category] += price
  return category_prices

def find_products_by_category(data, category):

  pattern = rf"\b{category.lower()}\b|\b(?!.*{category.lower()})\w+\b" 

  matching_products = []
  for product in data:
    product_line = f"{product['id']}:{product['name']}:{product['description']}:{product['category']}:{product['price']}\n"
    if re.search(pattern, product_line, re.IGNORECASE): 
      matching_products.append(product)
  return matching_products



# a. Read product data from file (assuming productdata.txt exists)
product_data = read_product_data("productdata.txt")

# b. Calculate sum of prices for each category
category_sums = calculate_price_sum_by_category(product_data)
print("\nSum of prices for each category:")
for category, total_price in category_sums.items():
  print(f"{category}→{total_price}")

# c. User input for category and product search
category = input("\nEnter category: ")

matching_products = find_products_by_category(product_data, category)

if matching_products:
  print(f"\nProducts in category '{category}':")
  for product in matching_products:
    print(f"{product['id']}:{product['name']}:{product['description']}:{product['category']}:{product['price']}")
else:
  print(f"\nNo products found in category '{category}'.")


# In[ ]:





# In[ ]:




