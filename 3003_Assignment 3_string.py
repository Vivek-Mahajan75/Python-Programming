#!/usr/bin/env python
# coding: utf-8

# ### Q1) Write a program that asks the user how many days are in a month, and what day of the
# ### week the month begins on (0 for Monday, 1 for Tuesday, etc), and then prints a calendar for that 
# ### month.
# ### For example, here is the output for a 31-day month that begins on day 5 (Saturday):

# In[6]:


while True:
    numdays=int(input("Enter days"))
    if numdays>=28 and numdays<=31:
        break
while True:
    startday=int(input("Enter start day 0-Mon 1-Tues 2-Wed 3-Thur 4-Fri 5-Sat 6-Sun"))
    if startday>=0 and startday<=6:
        break
print("Mon\t Tues\t Wed\t Thur\t Fri\t Sat\t Sun")
print("   \t"*startday,end=" ")
count=startday
for i in range(1,numdays+1):
    print(" "+str(i),end="\t")
    count=count+1
    if count==7:
        print()
        count=0


# In[ ]:





# ### Q2) Define a procedure histogram() that takes a list of integers and prints a histogram to the 
# ### screen. 
# For example, histogram([4, 9, 7]) should print the following:
# ****
# *********
# *******

# In[44]:


list1=[4, 9, 7]

def histogram(list1):
    for i in list1:
         print("*"*i)
histogram(list1)


# In[ ]:





# ### Q3) Write a version of a palindrome recognizer that also accepts phrase palindromes such as 
# 
# "Go hang a salami I'm a lasagna hog.", "Was it a rat I saw?", "Step on no pets", "Sit on a 
# 
# potato pan, Otis", "Lisa Bonet ate no basil", "Satan, oscillate my metallic sonatas", "I roamed 
# 
# under it as a tired nude Maori", "Rise to vote sir", or the exclamation "Dammit, I'm mad!".
# 
# Note that punctuation, capitalization, and spacing are usually ignored.

# In[26]:


def is_palindrome(text):
    cleaned_text = "".join(char.lower() for char in text if char.isalnum())
    return cleaned_text == cleaned_text[::-1]

phrases = [
  "Go hang a salami I'm a lasagna hog",
  "Was it a car I saw, evil sir I saw a car",
  "Step on no pets"
]

for phrase in phrases:
    if is_palindrome(phrase):
        print(f"'{phrase}' is a palindrome.")
    else:
        print(f"'{phrase}' is not a palindrome.")


# In[ ]:





# ### Q4) A pangram is a sentence that contains all the letters of the English alphabet at least once, 
# for example: The quick brown fox, jumps over the lazy dog!!!!.
# 
# Your task here is to write a function to check a sentence to see if it is a pangram or not.

# In[29]:


import string

def is_pangram(sentence):
    return set(char.lower() for char in sentence if char.isalnum()) == set(string.ascii_lowercase)

sentences = [
  "The quick brown fox jumps over the lazy dog",  # Pangram
  "This is not a pangram",
  "Waltz, bad nymph, for quick jigs vex me much."]

for sentence in sentences:
    if is_pangram(sentence):
        print(f"'{sentence}' is a pangram.")
    else:
        print(f"'{sentence}' is not a pangram.")


# In[ ]:





# ### Q5) Write a function translate() that will translate a text into "rövarspråket" (Swedish for "robber's 
# ### language").
# That is, double every consonant and place an occurrence of "o" in between.
# 
# For example, translate("this is fun") should return the string "tothohisos isos fofunon"

# In[38]:


def translate_to_rovarspraket(text):
    vowels = "aeiouyåäö"
    translated_text = ""
    for char in text.lower():
        if char.isalpha():  
            if char in vowels:
                translated_text += char
            else:
                translated_text += char + "o" + char
        else:
            translated_text += char  

    return translated_text

text = "rövarspråket"
translated_text = translate_to_rovarspraket(text)
print(translated_text) 


# In[ ]:





# ### Q6) Write a program that contains a function that has one parameter, n, representing an integer 
# ### greater than 0. The function should return n! (n factorial). Then write a main function that calls 
# ### this function with the values 1 through 20, one at a time.

# In[14]:


def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def main():   
    for i in range(1,21):
        result = factorial(i)
        print(result)
if __name__ == "__main__":
    main()


# In[ ]:





# ### Q7) Write a recursive sum from 1 to x (i.e. 1 + 2 + ... + x) recursively as follows for integer x ≥ 1:
# 1, if x = 1
# 
# x + sum from 1 to x-1 if x > 1
# 
# Complete the following Python program to compute the sum 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 
# + 10
# 
#  def sum(x):
#  
#  you complete this function recursively
#  
#  def main():
# 
#  compute and print 1 + 2 + ... + 10
#  
#  print(sum(10))
#  
#  main()

# In[10]:


def sum(x):
  if x == 1:
    return 1
  else:
    return x + sum(x - 1)
def main():

  total_sum = sum(10)

  print(f"The sum of 1 to 10 is: {total_sum}")
if __name__ == "__main__":
  main()


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




