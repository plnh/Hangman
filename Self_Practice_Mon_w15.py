#Problem 1

"""
You have a text and a list of words. You need to check if the words in a list appear in the same order as in the given text.

Cases you should expect while solving this challenge:

a word from the list is not in the text - your function should return False;
any word can appear more than once in a text - use only the first one;
two words in the given list are the same - your function should return False;
the condition is case sensitive, which means 'hi' and 'Hi' are two different words;
the text includes only English letters and spaces.
Input: Two arguments. The first one is a given text, the second is a list of words.

Output: A bool.

Example:

words_order('hi world im here', ['world', 'here']) == True
words_order('hi world im here', ['here', 'world']) == False
words_order('hi world im here', ['world']) == True
words_order('hi world im here',
 ['world', 'here', 'hi']) == False
words_order('hi world im here',
 ['world', 'im', 'here']) == True
words_order('hi world im here',
 ['world', 'hi', 'here']) == False
words_order('hi world im here', ['world', 'world']) == False
words_order('hi world im here',
 ['country', 'world']) == False
words_order('hi world im here', ['wo', 'rld']) == False
words_order('', ['world', 'here']) == False
"""

def words_order(text: str, words: list) -> bool:
    temp = 0
    my_list = text.split()
    for char in words:
        try:
            text_index = my_list.index(char)
            
        except ValueError:
            return False
            break
        if text_index >= temp:
            temp = text_index
            my_list.remove(char)
        else:
            return False
            break
    return True
"""
Other solution
"""
def words_order_NEW(text: str, words: list) -> bool:
    text_words = {w for w in text.split() if w in words}
    return list(sorted(text_words, key=text.index)) == words

#Problem 2

"""
You are given a list of files. You need to sort this list by the file extension. The files with the same extension should be sorted by name.

Some possible cases:

Filename cannot be an empty string;
Files without the extension should go before the files with one;
Filename ".config" has an empty extension and a name ".config";
Filename "config." has an empty extension and a name "config.";
Filename "table.imp.xls" has an extension "xls" and a name "table.imp";
Filename ".imp.xls" has an extension "xls" and a name ".imp".

Input: A list of filenames.

Output: A list of filenames.

Example:

sort_by_ext(['1.cad', '1.bat', '1.aa']) == ['1.aa', '1.bat', '1.cad']
sort_by_ext(['1.cad', '1.bat', '1.aa', '2.bat']) == ['1.aa', '1.bat', '2.bat', '1.cad']
sort_by_ext(['1.cad', '1.bat', '1.aa', '.bat']) == ['.bat', '1.aa', '1.bat', '1.cad']
sort_by_ext(['1.cad', '1.bat', '.aa', '.bat']) == ['.aa', '.bat', '1.bat', '1.cad']
sort_by_ext(['1.cad', '1.', '1.aa']) == ['1.', '1.aa', '1.cad']
sort_by_ext(['1.cad', '1.bat', '1.aa', '1.aa.doc']) == ['1.aa', '1.bat', '1.cad', '1.aa.doc']

"""
from typing import List

def sort_by_ext(files: List[str]) -> List[str]:
    
    noext =[]
    noname = []
    remain = []
    for file in sorted(files):
        if file.rfind('.') == -1 or file.rfind('.') == len(file) -1: 
            noext.append(file)
        elif file.rfind('.') == 0:
            noname.append(file)
        else:
            remain.append(file)
     
    
    return sorted(noname, key=lambda x:x[1::]) + noext + sorted(remain, key= lambda x:x[x.rfind('.')+1::])


#Problem 3 MULTIPLE DIGITS

"""
You are given a positive integer. Your function should calculate the product of the digits excluding any zeroes.

For example: The number given is 123405. The result will be 1*2*3*4*5=120 (don't forget to exclude zeroes).

Input: A positive integer.

Output: The product of the digits as an integer.

Example:

checkio(123405) == 120
checkio(999) == 729
checkio(1000) == 1
checkio(1111) == 1

"""

def checkio(number: int) -> int:
    
    if number == 0:
        return 0
    else:
        result = 1
    
    for i in str(number):
        if int(i) != 0:
            result *= int(i)
        else:
            continue
    
    return result


#Problem 4 ACCEPTABLE PASSWORD II

"""
In this mission you need to create a password verification function.

Those are the verification conditions:

the length should be bigger than 6;
should contain at least one digit.
Input: A string.

Output: A bool.

Example:

is_acceptable_password('short') == False
is_acceptable_password('muchlonger') == False
is_acceptable_password('ashort') == False
is_acceptable_password('ashort')  == True
is_acceptable_password('sh5') == False

"""


def is_acceptable_password(password: str) -> bool:
    
    
    return True if len(password) > 6 and any( char.isdigit() for char in password) else False


#Problem 5 ACCEPTABLE PASSWORD III

"""
In this mission you need to create a password verification function.

Those are the verification conditions:

the length should be bigger than 6;
should contain at least one digit, but cannot consist of just digits.
Input: A string.

Output: A bool.

Example:

is_acceptable_password('short') == False
is_acceptable_password('muchlonger') == False
is_acceptable_password('ashort') == False
is_acceptable_password('muchlonger5') == True
is_acceptable_password('sh5') == False
is_acceptable_password('1234567') == False

"""
def is_acceptable_passwordIII(password: str) -> bool:
    
    return True if len(password) > 6 and any(char.isdigit() for char in password) and password.isdigit() != True else False
    



# Problem 6 ACCEPTABLE PASSWORD IV

"""
In this mission you need to create a password verification function.

Those are the verification conditions:

the length should be bigger than 6;
should contain at least one digit, but it cannot consist of just digits;
having numbers or containing just numbers does not apply to the password longer than 9.
Input: A string.

Output: A bool.

Example:

is_acceptable_password('short') == False
is_acceptable_password('short54') == True
is_acceptable_password('muchlonger') == True
is_acceptable_password('ashort') == False
is_acceptable_password('muchlonger5') == True
is_acceptable_password('sh5') == False
is_acceptable_password('1234567') == False
is_acceptable_password('12345678910') == True

"""

def is_acceptable_passwordIV(password: str) -> bool:
    
    if len(password) > 9:
        return True
    else: 
        if len(password) > 6 and any(char.isdigit() for char in password) and password.isdigit() != True:
            return True
        else:
            return False
    

#Problem 7 ACCEPTABLE PASSWORD V

"""

In this mission you need to create a password verification function.

Those are the verification conditions:

the length should be bigger than 6;
should contain at least one digit, but it cannot consist of just digits;
having numbers or containing just numbers does not apply to the password longer than 9.
a string should not contain the word "password" in any case.
Input: A string.

Output: A bool.

Example:

is_acceptable_password('short') == False
is_acceptable_password('short54') == True
is_acceptable_password('muchlonger') == True
is_acceptable_password('ashort') == False
is_acceptable_password('muchlonger5') == True
is_acceptable_password('sh5') == False
is_acceptable_password('1234567') == False
is_acceptable_password('12345678910') == True
is_acceptable_password('password12345') == False
is_acceptable_password('PASSWORD12345') == False
is_acceptable_password('pass1234word') == True


"""

def is_acceptable_passwordV(password: str) -> bool:
    
    if password.casefold().find('password') > -1:
        return False
    else:    
        if len(password) > 9:
            return True
        else: 
            if len(password) > 6 and any(char.isdigit() for char in password) and password.isdigit() != True:
                return True
            else:
                return False
    
#Problem 8 ACCEPTABLE PASSWORD VI

"""
In this mission you need to create a password verification function.

Those are the verification conditions:

the length should be bigger than 6;
should contain at least one digit, but it cannot consist of just digits;
having numbers or containing just numbers does not apply to the password longer than 9.
a string should not contain the word "password" in any case;
should contain 3 different letters (or digits) even if it is longer than 10
Input: A string.

Output: A bool.

Example:

is_acceptable_password('short') == False
is_acceptable_password('short54') == True
is_acceptable_password('muchlonger') == True
is_acceptable_password('ashort') == False
is_acceptable_password('muchlonger5') == True
is_acceptable_password('sh5') == False
is_acceptable_password('1234567') == False
is_acceptable_password('12345678910') == True
is_acceptable_password('password12345') == False
is_acceptable_password('PASSWORD12345') == False
is_acceptable_password('pass1234word') == True
is_acceptable_password('aaaaaa1') == False
is_acceptable_password('aaaaaabbbbb') == False
"""
def is_acceptable_passwordVI(password: str) -> bool:
    
    my_list = []
    for i in range(len(password)):
        if password[i] not in my_list:
            my_list.append(password[i])
    if len(my_list) < 3:
        return False
    else:
        if password.casefold().find('password') > -1:
            return False
        else:    
            if len(password) > 9:
                return True
            else: 
                if len(password) > 6 and any(char.isdigit() for char in password) and password.isdigit() != True:
                    return True
                else:
                    return False


"""
other solution

"""
def is_acceptable_passwordVI_New(password: str) -> bool:
    
    a = len(password) > 9
    b = len(password) >= 6
    v = len(set(password)) >= 3
    x = "password" not in password.lower() 
    y = bool([el for el in password if el.isdigit()])
    z = bool([el for el in password if el.isalpha()])
    return ((b and y and z) or a) and x and v



#Problem 9 All UPPERCASE


"""
Check if a given string has all symbols in upper case. If the string is empty or doesn't have any letter in it - function should return False.

Input: A string.

Output: a boolean.

Example:

is_all_upper('ALL UPPER') == True
is_all_upper('all lower') == False
is_all_upper('mixed UPPER and lower') == False
is_all_upper('') == False

"""

def is_all_upper(text: str) -> bool:
    # your code here
    return text.isupper()


#Problem 10 ASCENDIN LIST

"""
Determine whether the sequence of elements items is ascending so that its each element is strictly larger than (and not merely equal to) the element that precedes it.

Input: Iterable with ints.

Output: Bool.

Example:

is_ascending([-5, 10, 99, 123456]) == True
is_ascending([99]) == True
is_ascending([4, 5, 6, 7, 3, 7, 9]) == False
is_ascending([]) == True
is_ascending([1, 1, 1, 1]) == False

"""
from typing import Iterable

def is_ascending(items: Iterable[int]) -> bool:
    if len(items) < 2:
        return True
    else:
        for i in range(len(items) - 1):
            if items[i] < items[i+1]:
                continue
            else:
                return False
                break
    return True


"""
other solution
"""

def is_ascending_new(items: Iterable[int]) -> bool:
    
    return not any([ items[i] <= items[i-1] for i in range(1,len(items)) ])
    """ Value index return empty list """ 
    
    
