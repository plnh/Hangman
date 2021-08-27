# Follow throw tutorial 
"""
https://www.youtube.com/watch?v=LzYNWme1W6Q&list=WL&index=9&t=8669s&ab_channel=Amigoscode
"""

# I am a comment


# name, age = 'Jamile', 20
# isAdult = True
# print(name,age)
# print(type(name))
# print(type(age))
# print(type(isAdult))

# brand: str = 'Toyota'
# print(len(brand))
# print(brand != 'toyota') #case sensitive
# print('yo' in brand) 
# print('yo' not in brand)


# #multiple lines
# comment = """
# asdas
# dasdasd
# asdasd
# """
        
        
# print(comment)

# name = 'Jamila'
# email = """
# hello {}
# how are you? {}
# It was nice talking to you
# """

# print(email.format(name,name))

# name = 'Jamila'
# email = f"""
# hello {name}
# how are you? 
# It was nice talking to you
# {age}
# """

# print(email)

# # indentation
# def my_function():
#     name = 'Maria'
#     surname = 'Jamila'
    
# # Reserved keywords
# import keyword
# print(keyword.kwlist)


# # Logical Operators

# print(10 > 5) and print (1 > 3) #there is a dif between those
# print( 10 > 5 and 1> 3)
# print((10>5) and (1>3) and ('A' == 'a'))

# print(not('James' == 'Jane'))

# #Assignemt operators

# car = 'Toyota'
# print(car)
# car = 'Honda'
# print(car)
# car += 'hudai'
# print(car)
# car *=2
# print(car)


# number = 0
# print(number)
# number += 3
# print(number)
# number **= 2
# print(number)


# # If statement

# number = -5

# if number > 0:
#     print(f"{number} is possitive")
# elif number == 0:
#     print(number)
# else:
#     print(f"{number} is negative")


# # Ternary if statement
# number = 10 
# message = 'possitive' if number > 0 else '0 or negative' #only use when only 1 if then else
# print(message)


# # Lists
# print(type([]))

# myList = [1, 2, 3, 4, 'hurry', 1 + 4, ['a','b','c']]

# print(myList)
# print(myList[0]) #index
# print(myList[6][1])

# numbers = [1,4,1, 6,2]
# print(numbers)

# numbers.reverse()
# print(numbers)

# numbers.sort()
# print(numbers)

# numbers.append(100)
# print(numbers)

# numbers.remove(1) #only remove the 1st instant
# print(numbers)

# numbers.pop()
# print(numbers)

# del numbers[1:3] # remove from index 1 and index 2
# print(numbers)

# numbers.clear()
# print(numbers)
# print( 4 in numbers)


# # Sets

# myList = [1, 1]
# mySet = {1, 1,2}
# lettersSet = {'A', 'A', 'B', 'B', 'C', 'C'}

# print(myList)
# print(mySet) # dulplicate is not allowed in set

# print(mySet.pop())

# lettersSet = {'A', 'A', 'B', 'B', 'C', 'C'}
# print(lettersSet) # Set is unorder. Different order will happend each time we print

# lettersA = {'A', 'B', 'C'}
# lettersB = {'E', 'F'}

# union = lettersA | lettersB
# print(lettersA | lettersB) #unions

# intersection = lettersA & lettersB
# print(intersection) #intersection 

# lettersA = {'A', 'B', 'C'}
# lettersB = {'A', 'E', 'F'}

# intersection = lettersA & lettersB
# print(intersection) #intersection 

# # Dictionaries

# person = { 'name': 'Ha', 'age' : 30, 'address' : 'France'}

# print(person['name']) # name is key, Ha is value
# print(person['age'])
# print(person['address'])


# print(person.keys())
# print(person.values())
# #person.clear()
# print(person.get('age')) # getter method not impact the values inside

# person['age'] = 100 #update the value
# print(person)

# # FOR Loop


# names = {'John', 'Anna', 'Trevor', 'Jamila'}

# for name in names:
#     print(name)
    

# Loop through Dictionary

# person = { 'name': 'Ha', 'age' : 30, 'address' : 'France'}

# for key in person:
#     print(f"key: {key} value: {person[key]}")

# for key, value in person.items():
#     print(f"key: {key} value: {value}") # no need to call value through person[key]
    


# # Exercise
# numbers = [1,3,5,7,8]
# result = 0
# for number in numbers:
#     result += number
# print(f"Result= {result}")


# WHILE Loop
# number = 0
# while number < 10:
#     print(number)
#     number+= 1
# else:
#     print('While Loop ended')
    
    
# Break and Continue

# number = 0
# while number < 10:
#     number += 1
#     if number <= 5:
#         continue
#     print(number)
    
# for n in range(0,11):
#     if n <= 5:
#         continue
#     print(n)

# for n in range(0,11):
#     if n <= 5:
#         break
#     print(n)


# Function
# Parameters and Arguments

# def greet(name, age =-1):  
#     print(f'Hello {name}')
#     if not age < 0:
#         print(f'I know you are {age} years old')
# greet('Ha')
# greet('John', 3)


# Return values from function

# def is_adult(age):
#     if not age < 16:
#         return True
#     else:
#         return False

# def is_adult(age):
#     return not age < 16


# def convertGender(gender= 'unknown'):
#     if gender.upper() == 'M':
#         return 'Male'
#     elif gender.upper() == 'F':
#         return 'Felmale'
#     else:
#         return 'unknown'

#Built-in Function and Import Statement

import math
print(math.pi)










































































