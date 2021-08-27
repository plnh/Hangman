# -*- coding: utf-8 -*-

#Problem 1

"""
Sort the given iterable so that its elements end up in the decreasing frequency order, that is, the number of times they appear in elements. If two elements have the same frequency, they should end up in the same order as the first appearance in the iterable.

Input: Iterable

Output: Iterable

Precondition: elements can be ints or strings
"""

def frequency_sort(items):
    frequencies = dict()
    result = []
   
    for key in items:
        if key not in frequencies:
            frequencies[key] = 1
        else:
            frequencies[key] += 1
   
    
    for key in sorted(frequencies.items(), key=lambda x:x[1], reverse = True):
        i = 0
        while i < key[1]:
            result.append(key[0])
            i += 1
    
    return result

""" 
Other solution

"""

def frequency_sort_NEW(items):
    frequencies = {key: items.count(key) for key in items}
    result = []
    for item, amount in sorted(frequencies.items(), key= lambda x: (x[1], -items.index(x[0])), reverse=True):
        result.extend([item] * amount)
    return result

#Problem 2

"""

Input: Placed pawns coordinates as a set of strings.

Output: The number of safe pawns as a integer.
Example:

safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1

"""


def safe_pawns(pawns: set) -> int:
    pawns_indexes = set()
    for p in pawns:
        col = ord(p[0]) - 97
        row = int(p[1]) - 1
        pawns_indexes.add((col,row))
    
    count = 0
    for p in pawns_indexes:
        p_left = (p[0]-1,p[1]-1)
        p_right = (p[0]+1,p[1]-1)
        if p_left in pawns_indexes or p_right in pawns_indexes:
            count += 1
            
    return count


"""
Other solution

"""

def safe_pawns_NEW(pawns : set)-> int:
    count = 0
    for i in pawns:
        if chr(ord(i[0])+1)+str(int(i[1])-1) in pawns or chr(ord(i[0])-1)+str(int(i[1])-1) in pawns:
            count+=1
    return count

#Problem 3
"""
Input: The time of the day.

Output: The angle of the sun, rounded to 2 decimal places.

Example:

sun_angle("07:00") == 15
sun_angle("12:15"] == 93.75
sun_angle("01:23") == "I don't see the sun!"

"""


def sun_angle(time):
    a= (int(time[:2:]) - 6) *60 + int(time[3::]) 
    if a>= 0 and a<= 12*60:
        angle = a * 180 / (12*60)
    else:
        return "I don't see the sun!"
    return round(angle,2)


#Problem 4

"""

Input: Array.

Output: Array or two arrays.

Example:

split_list([1, 2, 3, 4, 5, 6]) == [[1, 2, 3], [4, 5, 6]]
split_list([1, 2, 3]) == [[1, 2], [3]]

"""

def split_list(items: list) -> list:
    return[ items[:int(len(items) - len(items)//2):] , items[int(len(items)-len(items)//2)::] ]



#Problem 5

"""
In this mission you should check if all elements in the given list are equal.

Input: List.

Output: Bool.

Example:

all_the_same([1, 1, 1]) == True
all_the_same([1, 2, 1]) == False
all_the_same(['a', 'a', 'a']) == True
all_the_same([1, 2, 1]) == True

"""

def all_the_same(elements):
    if elements == []:
        return True
    else:
        return elements.count(elements[0]) == len(elements) 


#Problem 6

"""
Computer date and time format consists only of numbers, for example: 21.05.2018 16:30
Humans prefer to see something like this: 21 May 2018 year, 16 hours 30 minutes
Your task is simple - convert the input date and time from computer format into a "human" format.

example

Input: Date and time as a string

Output: The same date and time, but in a more readable format

Example:

date_time("01.01.2000 00:00") == "1 January 2000 year 0 hours 0 minutes"
date_time("19.09.2999 01:59") == "19 September 2999 year 1 hour 59 minutes"
date_time("21.10.1999 18:01") == "21 October 1999 year 18 hours 1 minute"
# NB: words "hour" and "minute" are used only when time is 01:mm (1 hour) or hh:01 (1 minute).
# In other cases it should be used "hours" and "minutes".

"""
import datetime

def date_time(time: str) -> str:
    a = datetime.datetime(int(time[6:10:]), int(time[3:5:]), int(time[:2:]), int(time[11:13:]), int(time[14::]))
    h = 'hours'
    m = 'minutes'
    if int(time[11:13:]) == 1:
        h = h.rstrip('s')
    if int(time[14::]) == 1:
        m = m.rstrip('s')
    return a.strftime('%d').lstrip('0')+' '+a.strftime('%B')+' '+a.strftime('%Y')+' year '+str(int(a.strftime('%H'))) +' '+h+' '+str(int(a.strftime('%M')))+' '+m


#Problem 7

"""
Your task is to decrypt the secret message using the Morse code.
The message will consist of words with 3 spaces between them and 1 space between each letter of each word.
If the decrypted text starts with a letter then you'll have to print this letter in uppercase.

example

Input: The secret message.

Output: The decrypted text.

Example:

morse_decoder("... --- -- .   - . -..- -") == "Some text"
morse_decoder("..--- ----- .---- ---..") == "2018"
morse_decoder(".. -   .-- .- ...   .-   --. --- --- -..   -.. .- -.--") == "It was a good day"

"""

MORSE = {'.-':    'a', '-...':  'b', '-.-.':  'c',
         '-..':   'd', '.':     'e', '..-.':  'f',
         '--.':   'g', '....':  'h', '..':    'i',
         '.---':  'j', '-.-':   'k', '.-..':  'l',
         '--':    'm', '-.':    'n', '---':   'o',
         '.--.':  'p', '--.-':  'q', '.-.':   'r',
         '...':   's', '-':     't', '..-':   'u',
         '...-':  'v', '.--':   'w', '-..-':  'x',
         '-.--':  'y', '--..':  'z', '-----': '0',
         '.----': '1', '..---': '2', '...--': '3',
         '....-': '4', '.....': '5', '-....': '6',
         '--...': '7', '---..': '8', '----.': '9',
        }

def morse_decoder(code):
    text =[]
 
    
    for char in code.split(' '):
       
        text.append(MORSE.get(char, ' '))
    return ' '.join((''.join(text)).split()).capitalize()

"""
Other solution
"""
MORSE = {'.-':    'a', '-...':  'b', '-.-.':  'c',
         '-..':   'd', '.':     'e', '..-.':  'f',
         '--.':   'g', '....':  'h', '..':    'i',
         '.---':  'j', '-.-':   'k', '.-..':  'l',
         '--':    'm', '-.':    'n', '---':   'o',
         '.--.':  'p', '--.-':  'q', '.-.':   'r',
         '...':   's', '-':     't', '..-':   'u',
         '...-':  'v', '.--':   'w', '-..-':  'x',
         '-.--':  'y', '--..':  'z', '-----': '0',
         '.----': '1', '..---': '2', '...--': '3',
         '....-': '4', '.....': '5', '-....': '6',
         '--...': '7', '---..': '8', '----.': '9'
        }

def morse_decoder(code):
    code = code.replace('   ', ' | ')
    tl = [MORSE[i] if i != '|' else ' ' for i in code.split(' ')]
    return ''.join(tl).capitalize()

























