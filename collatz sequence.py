# -*- coding: utf-8 -*-
"""
automate boring stuff with Python
"""

def collatz(n):
    while n != 1:
        if n % 2 == 1:
            n = (3*n +1)
            print(n)
        else:
            n = n/2
            print(n)
        

print('Type a number ...')
try:
    n = int(input())
except ValueError:
    print('Please enter a VALID integer')
    
collatz(n)