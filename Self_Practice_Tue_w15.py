# Problem 1 SIMILAR TRIANGLES
"""
This is a mission to check the similarity of two triangles.

You are given two lists as coordinates of vertices of each triangle.
You have to return a bool. (The triangles are similar or not)

Example:

similar_triangles([(0, 0), (1, 2), (2, 0)], [(3, 0), (4, 2), (5, 0)]) is True
similar_triangles([(0, 0), (1, 2), (2, 0)], [(3, 0), (4, 3), (5, 0)]) is False
similar_triangles([(1, 0), (1, 2), (2, 0)], [(3, 0), (5, 4), (5, 0)]) is True


similar_triangles([(0, 0), (1, 2), (2, 0)], [(3, 0), (4, 2), (5, 0)]) is True, 'basic'
similar_triangles([(0, 0), (1, 2), (2, 0)], [(3, 0), (4, 3), (5, 0)]) is False, 'different #1'
similar_triangles([(0, 0), (1, 2), (2, 0)], [(2, 0), (4, 4), (6, 0)]) is True, 'scaling'
similar_triangles([(0, 0), (0, 3), (2, 0)], [(3, 0), (5, 3), (5, 0)]) is True, 'reflection'
similar_triangles([(1, 0), (1, 2), (2, 0)], [(3, 0), (5, 4), (5, 0)]) is True, 'scaling and reflection'
similar_triangles([(1, 0), (1, 3), (2, 0)], [(3, 0), (5, 5), (5, 0)]) is False, 'different #2'
"""

from typing import List, Tuple
Coords = List[Tuple[int, int]]
import math

def similar_triangles(coords_1: Coords, coords_2: Coords) -> bool:
    
    tri_1 = [math.dist(coords_1[0],coords_1[1]),math.dist(coords_1[0],coords_1[2]),math.dist(coords_1[2],coords_1[1])]
    tri_2 = [math.dist(coords_2[0],coords_2[1]),math.dist(coords_2[0],coords_2[2]),math.dist(coords_2[2],coords_2[1])]
    a = sorted(tri_1)[0] / sorted(tri_2)[0]
    b = sorted(tri_1)[1] / sorted(tri_2)[1]
    c = sorted(tri_1)[2] / sorted(tri_2)[2]
    return True if a == b == c else False
    

#Problem 2  Unix Match. Part 1

"""
Sometimes you find yourself in a situation when, among a huge number of files on your computer or in a separate folder, 
you need to find files of a certain type. For example, images with the extension '.jpg' or documents with the extension '.txt', 
or even files that have the word 'butterfly' in their name. Doing this manually can be time-consuming. 
'Matching' or patterns for searching files by a specific mask are just what you need for these sort of challenges.
This mission will help you understand how this works.

You need to find out if the given unix pattern matches the given filename.

Let me show you what I mean by matching the filenames in the unix-shell. For example, * matches everything and *.txt matches all of the files that have txt extension. Here is a small table that shows symbols that can be used in patterns.

*	matches everything
?	matches any single character
Input: Two arguments. Both are strings.

Output: Bool.

Example:

unix_match('somefile.txt', '*') == True
unix_match('other.exe', '*') == True
unix_match('my.exe', '*.txt') == False
unix_match('log1.txt', 'log?.txt') == True
unix_match('log12.txt', 'log?.txt') == False
unix_match('log12.txt', 'log??.txt') == True

"""
def unix_match(filename: str, pattern: str) -> bool:
    keys = ''.join(pattern.replace('*',' ').split())
    
    if keys == '':
        return True
    elif len(pattern) > len(filename):
        return False
    elif '*' not in pattern:
        for i in range(len(filename)):
            if filename[i] != pattern[i] and pattern[i] != '?':
                return False
                break
        return True
    else:
        for i in keys:
            
            if i != '?' and filename.find(i) == -1:
                
                return False
                break
        return True

# Problem 3 Unixmatch. Part 2
"""
Sometimes you find yourself in a situation when, among a huge number of files on your computer or in a separate folder, you need to find files of a certain type. For example, images with the extension '.jpg' or documents with the extension '.txt', or even files that have the word 'butterfly' in their name. Doing this manually can be time-consuming. 'Matching' or patterns for searching files by a specific mask are just what you need for these sort of challenges.
This mission will help you understand how this works.

You need to find out if the given unix pattern matches the given filename.

Here is a small table that shows symbols that can be used in patterns.

[seq]	matches any character in seq, for example [123] means any character - '1', '2' or '3'
[!seq]	matches any character not in seq, for example [!123] means any character except '1', '2' and '3'
[]	seq without any chars will never match
Note that the expression in one pair of square brackets responds only for 1 character. So

('0123', '[!abc]123') == True, but ('00123', '[!abc]123') = False
Input: Two arguments. Both are strings.

Output: Bool.

Example:

unix_match('somefile.txt', 'somefile.txt') == True
unix_match('1name.txt', '[!abc]name.txt') == True
unix_match('log1.txt', 'log[1234567890].txt') == True

"""
            
def between_marker(text,a,b):
    if a in text:
        first = text.find(a)+1
    else:
        first = 0
    
    if b in text:
        last = text.find(b)
    else:
        last = len(text)
    
    return text[first:last]

def check_table(char: str,key: list):
        if '!' in key:
            return char not in key
        else:
            return char in key

def unix_match1(filename: str, pattern: str) -> bool:
    
    keys = between_marker(pattern,'[',']')
    answer = True
    
    if '[' in pattern:
        pattern = ''.join(pattern[:pattern.index("[")] + '*' + pattern[pattern.index("]")+1:])
     
        
    if len(pattern) > len(filename):
        answer = False
        print(pattern)
    else:
        for i in range(len(filename)):
            
            if filename[i] == pattern[i]:
                answer = True
            elif pattern[i] == '*':
                answer = check_table(filename[i],keys)
                if answer == False:
                    break
            else:
                answer = False
                break

    return answer                
    
           
        
        

    
            
     
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            

    



