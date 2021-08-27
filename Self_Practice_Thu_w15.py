# Problem 1 Exercise 5.2 page 48
"""

Fermat’s Last Theorem says that there are no positive integers a, b, and c such that
    a^n + b^n = c^n
for any values of n greater than 2.
1. Write a function named check_fermat that takes four parameters—a, b, c and n—and
checks to see if Fermat’s theorem holds. If n is greater than 2 and
    a^n + b^n = c^n
the program should print, “Holy smokes, Fermat was wrong!” Otherwise the program should
print, “No, that doesn’t work.”
2. Write a function that prompts the user to input values for a, b, c and n, converts them to
integers, and uses check_fermat to check whether they violate Fermat’s theorem.
"""

def check_fermat(a,b,c,n):
    if a**n + b**n == c**n:
        print('Holy smokes, Fermat was wrong!')
    else:
        print('No, that doesn\'t work.')
        
def test_fermat():
    a = input('Type a number: ')
    b = input('Type an another one: ')
    c= input('one last one: ')
    n= input(' and a number larger than 2: ')
    
    check_fermat(int(a),int(b),int(c),int(n))
    

# Problem 2 Ecercise 5.3 page 48
"""
Exercise 5.3. If you are given three sticks, you may or may not be able to arrange them in a triangle.
For example, if one of the sticks is 12 inches long and the other two are one inch long, you will not
be able to get the short sticks to meet in the middle. For any three lengths, there is a simple test to
see if it is possible to form a triangle:
If any of the three lengths is greater than the sum of the other two, then you cannot
form a triangle. Otherwise, you can. (If the sum of two lengths equals the third, they
form what is called a “degenerate” triangle.)
1. Write a function named is_triangle that takes three integers as arguments, and that prints
either “Yes” or “No”, depending on whether you can or cannot form a triangle from sticks
with the given lengths.
2. Write a function that prompts the user to input three stick lengths, converts them to integers,
and uses is_triangle to check whether sticks with the given lengths can form a triangle.

"""

def check_triangle(a,b,c):
    max_length = max(a,b,c)
    min_length = min(a,b,c)
    mid_length = a+b+c - max_length - min_length
    if max_length > (min_length + mid_length):
        print('No')
    else:
        print('Yes')
def form_tri():
    a = input('Enter a lenght ')
    b = input('Enter a lenght ')
    c = input('Enter a lenght ')
    check_triangle(int(a), int(b), int(c))
    

        
        