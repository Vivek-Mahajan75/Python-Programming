#!/usr/bin/env python
# coding: utf-8

# ### Q1) Define a procedure histogram() that takes a list of integers and prints a histogram to the 
# ### screen. 
# For example, histogram([4, 9, 7]) should print the following:
# ****
# *********
# *******

# In[1]:


list1=[4, 9, 7]

def histogram(list1):
    for i in list1:
         print("*"*i)
histogram(list1)


# In[ ]:





# ### Q2) Write a version of a palindrome recognizer that also accepts phrase palindromes such as 
# 
# "Go hang a salami I'm a lasagna hog.", "Was it a rat I saw?", "Step on no pets", "Sit on a 
# 
# potato pan, Otis", "Lisa Bonet ate no basil", "Satan, oscillate my metallic sonatas", "I roamed 
# 
# under it as a tired nude Maori", "Rise to vote sir", or the exclamation "Dammit, I'm mad!". 
# 
# Note that punctuation, capitalization, and spacing are usually ignored.

# In[2]:


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





# ### Q3) A pangram is a sentence that contains all the letters of the English alphabet at least once
# 
# for example: The quick brown fox, jumps over the lazy dog!!!!. 
# 
# Your task here is to write a function to check a sentence to see if it is a pangram or not.

# In[3]:


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





# ### Q4) Write a function translate() that will translate a text into "rövarspråket" (Swedish for "robber's 
# ### language").
# 
# That is, double every consonant and place an occurrence of "o" in between. 
# 
# For example, translate("this is fun") should return the string "tothohisos isos fofunon".

# In[4]:


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





# ### Q5) Write a program that contains a function that has one parameter, n, representing an integer 
# ### greater than 0. The function should return n! (n factorial). Then write a main function that calls 
# ### this function with the values 1 through 20, one at a time, printing the returned results. 

# In[53]:


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





# ### Q6) Write a recursive sum from 1 to x (i.e. 1 + 2 + ... + x) recursively as follows for integer x ≥ 1:
# 1, if x = 1
# 
# x + sum from 1 to x-1 if x > 1
# 
# Complete the following Python program to compute the sum 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10
# 
# def main():
# 
# compute and print 1 + 2 + ... + 10
#   
# print sum(10)
#  
# def sum(x):
# 
# you complete this function recursively
#   
# main()

# In[40]:


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





# ### Q7) Define a function overlapping() that takes two lists and returns True if they have at least one
# ### member in common, False otherwise.
# 

# In[13]:


def overlapping(list1, list2):
    return any(item in list2 for item in list1)

list1 = [1, 2, 3, 4]
list2 = [7, 5, 6, 8]
if overlapping(list1, list2):
    print("The lists have overlapping elements:TRUE.")
else:
    print("The lists have no overlapping elements:FALSE.")


# In[ ]:





# ### Q8) Write a function find_longest_word() that takes a list of words and returns the length of the 
# ### longest one.

# In[21]:


def find_longest_words(words):
    if not words:
        return 0
    return max(len(word)for word in words)

words=["hello","the","list","has","overlaping","elements"]
longest_length=find_longest_word(words)
print(f"length of longest word:{longest_length}")


# In[ ]:





# ### Q9) Write a function filter_long_words() that takes a list of words and an integer n and returns the 
# ### list of words that are longer than n

# In[23]:


def filter_long_words(words, n):
    return [word for word in words if len(word) > n]  

words = ["Centre", "for", "development", "and", "advance", "computing", "Cdac"]
n = 4
long_words = filter_long_words(words, n)
print(f"Words longer than {n} characters: {long_words}")


# In[ ]:





# ### Q10)Define a simple "spelling correction" function correct() that takes a string and sees to it that
# 
# ### 1) two or more occurrences of the space character is compressed into one, and
# 
# ### 2) inserts an extra space after a period if the period is directly followed by a letter.
#  e.g. correct("This is very funny and cool.Indeed!")
#  should return "This is very funny and cool. Indeed!"

# In[38]:


import re
def correct(str1):
    t = re.sub(r'\s+'," ",str1)
    t2 = re.sub(r"\.([A-Za-z])",". \\1", t)
    return t
s = 'This is very               funny and cool. Indeed!'
correct(s)


# In[ ]:





# ### Q11) In English, present participle is formed by adding suffix -ing to infinite form: go -> going. A 
# ### simple set of heuristic rules can be given as follows:
# 
# If the verb ends in e, drop the e and add ing (if not exception: be, see, flee, knee, etc.)
# 
# If the verb ends in ie, change ie to y and add ing
# 
# For words consisting of consonant-vowel-consonant, double the final letter before adding 
# ing
# 
# By default just add ing
# 
# Your task in this exercise is to define a function make_ing_form() which given a verb in 
# infinitive form
# 
# returns its present participle form. Test your function with words such as lie, see, move and 
# hug.

# In[50]:


def make_ing_form(verb):
    exceptions = {"be": "being", "see": "seeing", "lie": "lying"}
    if verb in exceptions:
        return exceptions[verb]
    elif verb.endswith("e") and verb not in exceptions:
        return verb[:-1] + "ing"
    elif verb.endswith("ie"):
        return verb[:-2] + "ying"
    elif len(verb) > 2 and verb[-3] in 'aeiou' and verb[-2] not in 'aeiou':
        return verb + verb[-1] + "ing"
    else:
        return verb + "ing"

verbs = ["lie","see","move","hug","eat","be","listen","dance","write","speak","solve"]
for verb in verbs:
    ing_form = make_ing_form(verb)
    print(f"{verb} -> {ing_form}")


# In[ ]:





# In[ ]:





# In[ ]:




