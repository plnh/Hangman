# Problem 1 Replace Last
"""
In a given list the last element should become the first one. An empty list or list with only one element should stay the same

example

Input: List.

Output: Iterable.

Example:

replace_last([2, 3, 4, 1]) == [1, 2, 3, 4]
replace_last([1, 2, 3, 4]) == [4, 1, 2, 3]
replace_last([1]) == [1]
replace_last([]) == []
"""
from typing import Iterable

def replace_last(line) :
        
    return line[-1::] +  line[:-1:]


# Problem 2 INDEX POWER

"""
You are given an array with positive numbers and a number N. You should find the N-th power of the element in the array with the index N. If N is outside of the array, then return -1. Don't forget that the first element has the index 0.

Let's look at a few examples:
- array = [1, 2, 3, 4] and N = 2, then the result is 32 == 9;
- array = [1, 2, 3] and N = 3, but N is outside of the array, so the result is -1.

Input: Two arguments. An array as a list of integers and a number as a integer.

Output: The result as an integer.

Example:

index_power([1, 2, 3, 4], 2) == 9
index_power([1, 3, 10, 100], 3) == 1000000
index_power([0, 1], 0) == 1
index_power([1, 2], 3) == -1
        
1
2
3
4
5
How it is used: This mission teaches you how to use basic arrays and indexes when combined with simple mathematics.

Precondition: 0 < len(array) ≤ 10
0 ≤ N
all(0 ≤ x ≤ 100 for x in array)
"""

def index_power(array: list, n: int) -> int:
    
    return 

"""
Other solution
"""
def index_power1(array, n):
    try: return array[n] ** n
    except IndexError: return -1

# Problem 3 Majority
"""
We have a List of booleans. Let's check if the majority of elements are true.

example

Some cases worth mentioning: 1) an empty list should return false; 2) if trues and falses have an equal amount, function should return false.

Input: A List of booleans.

Output: A Boolean.

Example:

is_majority([True, True, False, True, False]) == True
is_majority([True, True, False]) == True
"""
def is_majority(items: list) -> bool:
    
    return True if items.count(True) > items.count(False) else False

# Problem 4 Remove All After
"""
Not all of the elements are important. What you need to do here is to remove all of the elements after the given one from list.

example

For illustration, we have an list [1, 2, 3, 4, 5] and we need to remove all the elements that go after 3 - which is 4 and 5.

We have two edge cases here: (1) if a cutting element cannot be found, then the list shouldn't be changed; (2) if the list is empty, then it should remain empty.

Input: List and the border element.

Output: Iterable (tuple, list, iterator ...).

Example:

remove_all_after([1, 2, 3, 4, 5], 3) == [1, 2, 3]
remove_all_after([1, 1, 2, 2, 3, 3], 2) == [1, 1, 2]
"""

from typing import Iterable


def remove_all_after(items: list, border: int) -> Iterable:
    try: 
        return items[:items.index(border)+1:]
    except ValueError:
        return items

# Problem 5 Median
"""
A median is a numerical value separating the upper half of a sorted array of numbers from the lower half. In a list where there are an odd number of entities, the median is the number found in the middle of the array. If the array contains an even number of entities, then there is no single middle value, instead the median becomes the average of the two numbers found in the middle. For this mission, you are given a non-empty array of natural numbers (X). With it, you must separate the upper half of the numbers from the lower half and find the median.

Input: An array as a list of integers.

Output: The median as a float or an integer.

Example:

checkio([1, 2, 3, 4, 5]) == 3
checkio([3, 1, 2, 5, 3]) == 3
checkio([1, 300, 2, 200, 1]) == 2
checkio([3, 6, 20, 99, 10, 15]) == 12.5

How it is used: The median has usage for Statistics and Probability theory, it has especially significant value for skewed distribution. For example: we want to know average wealth of people from a set of data -- 100 people earn $100 in month and 10 people earn $1,000,000. If we average it out, we get $91,000. This is weird value and does nothing to show us the real picture. In this case the median would give to us more useful value and a better picture. The Article at Wikipedia.

Precondition:
1 < len(data) ≤ 1000
all(0 ≤ x < 10 ** 6 for x in data)
"""

from typing import List

def checkio(data: List[int]) -> [int, float]:
    data = sorted(data)
    y = len(data)
    x = int(y//2)
    if int(y) % 2 != 0:
        return data[x]
    else:
        return (data[x] + data[x-1])/2














