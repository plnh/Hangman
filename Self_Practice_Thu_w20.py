# Chunk
"""
You have a lot of work to do, so you might want to split it into smaller pieces. This way you'll know which piece you'll do on Monday, which will be for Tuesday and so on.

Split a list into smaller lists of the same size (chunks). The last chunk can be smaller than the default chunk-size. If the list is empty, then you shouldn't have any chunks at all.

example

Input: Two arguments. A List and chunk size.

Output: An Iterable with chunked Iterable.

Example:

chunking_by([5, 4, 7, 3, 4, 5, 4], 3) == [[5, 4, 7], [3, 4, 5], [4]]
chunking_by([3, 4, 5], 1) == [[3], [4], [5]]
 
Precondition: chunk-size > 0
"""
from typing import Iterable


def chunking_by(items: list, size: int) -> Iterable:
    result = [] 
    for i in range(0, len(items), size):
        result.append(items[i:i + size])
    return result

# Sort Except Zero
"""
Sort the numbers in an array. But the position of zeros should not be changed.

Input: A List.

Output: An Iterable (tuple, list, iterator ...).

Example:

except_zero([5, 3, 0, 0, 4, 1, 4, 0, 7]) == [1, 3, 0, 0, 4, 4, 5, 0, 7]
except_zero([0, 2, 3, 1, 0, 4, 5]) == [0, 1, 2, 3, 0, 4, 5]
"""

from typing import Iterable


def except_zero(items: list) -> Iterable:
    index_list = []
    temps = []
    for n in range(len(items)):
        if items[n] == 0:
            index_list.append(n)
        else:
            temps.append(items[n])
            
    temps = sorted(temps)
    for n in index_list:
        temps.insert(n,0)
    
    return temps

# from typing import Iterable

# def except_zero(items: list) -> Iterable:
#     nums = iter(sorted([i for i in items if i != 0]))
#     return [next(nums) if n != 0 else 0 for n in items]



# Frequency Sorting
"""
Your mission is to sort the list by the frequency of numbers included in it. If a few numbers have an equal frequency - they should be sorted according to their natural order. For example: [5, 2, 4, 1, 1, 1, 3] ==> [1, 1, 1, 2, 3, 4, 5]

example

Input: Chaotic list of numbers.

Output: The list of numbers in which they are sorted by their frequency.

Example:

frequency_sorting([5, 3, 8, 11, 5, 6, 6, 5]) == [5, 5, 5, 6, 6, 3, 8, 11]

How it is used: For analyzing data using mathematical statistics and mathematical analysis, and for finding trends and predicting future changes (systems, phenomena, etc.)

Precondition:
array length <= 100
max number <= 100
"""
# def frequency_sorting(numbers):
#     temps = {}
#     for i in sorted(numbers):
#         if i not in temps:
#             temps[i] = numbers.count(i)
    
    
#     temps = {x: y for x, y in sorted(temps.items(), key=lambda item: item[1], reverse=True)}
#     result = []
#     for x in temps:
#         for i in range(temps.get(x)):
#             result.append(x)
    
#     return result


def checkio(numbers):
    return sorted(sorted(numbers), key=numbers.count, reverse=True)


# ZigZag






































