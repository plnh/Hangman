#Problem 1 Boolean Algebra

"""
In mathematics and mathematical logic, Boolean algebra is a sub-area of algebra in which the values of the variables are true or false, typically denoted with 1 or 0 respectively. Instead of elementary algebra where the values of the variables are numbers and the main operations are addition and multiplication, the main operations of Boolean algebra are the conjunction (denoted ∧), the disjunction (denoted ∨) and the negation (denoted ¬).

In this mission you should implement some boolean operations:
- "conjunction" denoted x ∧ y, satisfies x ∧ y = 1 if x = y = 1 and x ∧ y = 0 otherwise.
- "disjunction" denoted x ∨ y, satisfies x ∨ y = 0 if x = y = 0 and x ∨ y = 1 otherwise.
- "implication" (material implication) denoted x→y and can be described as ¬ x ∨ y. If x is true then the value of x → y is taken to be that of y. But if x is false then the value of y can be ignored; however the operation must return some truth value and there are only two choices, so the return value is the one that entails less, namely true.
- "exclusive" (exclusive or) denoted x ⊕ y and can be described as (x ∨ y)∧ ¬ (x ∧ y). It excludes the possibility of both x and y. Defined in terms of arithmetic it is addition mod 2 where 1 + 1 = 0.
- "equivalence" denoted x ≡ y and can be described as ¬ (x ⊕ y). It's true just when x and y have the same value.
Here you can see the truth table for these operations:

 x | y | x∧y | x∨y | x→y | x⊕y | x≡y |
--------------------------------------
 0 | 0 |  0  |  0  |  1  |  0  |  1  |
 1 | 0 |  0  |  1  |  0  |  1  |  0  |
 0 | 1 |  0  |  1  |  1  |  1  |  0  |
 1 | 1 |  1  |  1  |  1  |  0  |  1  |
--------------------------------------
You are given two boolean values x and y as 1 or 0 and you are given an operation name as described earlier. You should calculate the value and return it as 1 or 0.

Input: Three arguments. X and Y as 0 or 1. An operation name as a string.

Output: The result as 1 or 0.

Example:

boolean(1, 0, "conjunction") == 0
boolean(0, 1, "exclusive") == 1

Precondition: x in (0, 1)
y in (0, 1)
operation in ("conjunction", "disjunction", "implication", "exclusive", "equivalence")
"""

def boolean(x, y, operation):
    if operation == "conjunction":
        if x == 1 and y == 1:
            return 1
        else:
            return 0
        
    elif operation == "disjunction":
        if x == 0 and y == 0:
            return 0
        else:
            return 1
        
    elif operation == "implication":
        if x == 1 and y ==0:
            return 0
        else:
            return 1
        
    elif operation == "exclusive":
        if x == y:
            return 0
        else:
            return 1
        
    elif operation == "equivalence":
        if x == y:
            return 1
        else:
            return 0
    
    else:
        print('Invalid Command')
        
        
#Problem 2 BRACKETS
'''

You are given an expression with numbers, brackets and operators. For this task only the brackets matter. Brackets come in three flavors: "{}" "()" or "[]". Brackets are used to determine scope or to restrict some expression. If a bracket is open, then it must be closed with a closing bracket of the same type. The scope of a bracket must not intersected by another bracket. In this task you should make a decision, whether to correct an expression or not based on the brackets. Do not worry about operators and operands.

Input: An expression with different of types brackets as a string (unicode).

Output: A verdict on the correctness of the expression in boolean (True or False).

Example:

checkio("((5+3)*2+1)") == True
checkio("{[(3+1)+2]+}") == True
checkio("(3+{1-1)}") == False
checkio("[1+1]+(2*2)-{3/3}") == True
checkio("(({[(((1)-2)+3)-3]/3}-3)") == False
checkio("2+3") == True

How it is used: When you write code or complex expressions in a mathematical package, you can get a huge headache when it comes to excess or missing brackets. This concept can be useful for your own IDE.

Precondition:
There are only brackets ("{}" "()" or "[]"), digits or operators ("+" "-" "*" "/").
0 < len(expression) < 103       
'''

def checkio(expression):        

    for i in expression:
        if i not in '{}[]()':
            expression = expression.replace(i,'')
    
    while '[]' in expression or '{}' in expression or '()' in expression:
        expression = expression.replace('[]','')
        expression = expression.replace('{}','')
        expression = expression.replace('()','')
    return expression == ''
    
#Problem 3 FIND SEQUENCE
'''
You are given a matrix of NxN (4≤N≤10). You should check if there is a sequence of 4 or more matching digits. The sequence may be positioned horizontally, vertically or diagonally (NW-SE or NE-SW diagonals).

find-sequence
Input: A matrix as a list of lists with integers.

Output: Whether or not a sequence exists as a boolean.

Example:

checkio([
    [1, 2, 1, 1],
    [1, 1, 4, 1],
    [1, 3, 1, 6],
    [1, 7, 2, 5]
]) == True
checkio([
    [7, 1, 4, 1],
    [1, 2, 5, 2],
    [3, 4, 1, 3],
    [1, 1, 8, 1]
]) == False
checkio([
    [2, 1, 1, 6, 1],
    [1, 3, 2, 1, 1],
    [4, 1, 1, 3, 1],
    [5, 5, 5, 5, 5],
    [1, 1, 3, 1, 1]
]) == True
checkio([
    [7, 1, 1, 8, 1, 1],
    [1, 1, 7, 3, 1, 5],
    [2, 3, 1, 2, 5, 1],
    [1, 1, 1, 5, 1, 4],
    [4, 6, 5, 1, 3, 1],
    [1, 1, 9, 1, 2, 1]
    ]) == True

How it is used: This concept is useful for games where you need to detect various lines of the same elements (match 3 games for example). 
This algorithm can be used for basic pattern recognition.

Precondition:
0 ≤ len(matrix) ≤ 10
all(all(0 < x < 10 for x in row) for row in matrix)           
'''
from typing import List

def checkio1(matrix: List[List[int]]) -> bool: 

    maLen = len(matrix)    
    def seq_len(x,y,k,h,num):
        if x in range(maLen) and y in range(maLen) and matrix[x][y] == num:
            return 1 + seq_len(x+k,y+h,k,h,num)
        else:
            return 0

    rangeList = [[-1,-1],[-1,0],[-1,1],[0,1],[0,-1],[1,-1],[1,0],[1,1]]
                          
    for k, h in rangeList:
        
        for x in range(maLen):
            for y in range(maLen):
                result = seq_len(x,y,k,h,matrix[x][y])
                
                if result > 3:
                    return True
                
    return False
                
                
#Problem 4 Mathematically lucky tickets

'''       
The "Mathematically lucky tickets" concept is similar to the idea of the Russian "Lucky tickets". It refers to the old public transport tickets that had 6-digit numbers printed on them.

You are given a ticket number and the combination of its digits can become a mathematical expression by following these rules.

    1. The digits of the number can be split into groups of numbers.
    2. You cannot change the order of groups or digits.
    3. Each group is treated as a one integer number. (1 and 2 would become 12, etc.)
    4. Operational signs (+, -, * and /) are placed between the groups.
    5. Parenthesis are placed around subexpressions to eliminate any ambiguity
    in the evaluation order.

For example:

    * 238756 -> (2 * (38 + ((7 + 5) * 6)))
    * 000859 -> (0 + (00 + (8 + (5 + 9))))
    * 561403 -> (5 * (6 + (1 + (40 / 3))))

The ticket is considered mathematically lucky if no combination of its digits evaluates to 100. For example:

    * 000000 is obviously lucky, no matter which combination you construct it always
    evaluates to zero,
    * 707409 and 561709 are also lucky because they cannot evaluate to 100
    * 595347 is not lucky: (5 + ((9 * 5) + (3 + 47))) = 100
    * 593347 is not lucky: (5 + ((9 / (3 / 34)) - 7)) = 100
    * 271353 is not lucky: (2 - (7 * (((1 / 3) - 5) * 3))) = 100

The combination has to evaluate to 100 exactly to be counted as unlucky. Fractions can occur in intermediate calculations (like in above examples for 593347 and 271353) but the result must be an integer.

Task: Given a 6-digit number of the ticket, the program should determine whether it is mathematically lucky or not.

Input: 6 digits as a string.

Output: Is it mathematically lucky or not as a boolean.
        
'''


    
def operate(x,y):
    if y != 0:
        return [x+y,x-y,x*y,x/y]
    else:
        return [x+y,x-y,x*y]

def checklucky(data):
        
    N = len(data)
    gen = {}
    for l in range(1,N+1):
        hen = {}
        print(f"l is {l}")
        for i in range(0,N+1-l):
            
            hen[i, l] = set([int(data[i:i+l])])
            gen[i,l] = set([int(data[i:i+l])])
            computed = {}
            for k in range(1, l):
                for x in gen[i,k]:
                    for y in gen[i+k,l-k]:
                        computed[x,y] = set(operate(x,y))
                                    
            print(f"   i is {i}")
            print(f"   combination is {hen}")                       
            print(f"    computation is {computed}")
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        