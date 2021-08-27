#Problem 1  Unix Match. Part 1
#Other solution
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
import re

def unix_match(filename: str, pattern: str) -> bool:
    pattern = pattern.replace(".", "\.").replace("*", ".*").replace("?", ".")
    return False if re.match(r''+pattern+'', filename) == None else True



# Problem 2 Unixmatch. Part 2
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

unix_match1('somefile.txt', 'somefile.txt') == True
unix_match1('1name.txt', '[!abc]name.txt') == True
unix_match1('log1.txt', 'log[1234567890].txt') == True

"""
 
           
import re

def unix_match1(filename: str, pattern: str) -> bool:
    pattern = pattern.replace("*", "\\*").replace(".", "\\.").replace("[!", "[^").replace("[]", "[^.]").replace("[^]", "\[!\]")
    
    print(pattern)
    
    return True if re.match(pattern, filename) != None else False
  



""""
.       - Any Character Except New Line
\d      - Digit (0-9)
\D      - Not a Digit (0-9)
\w      - Word Character (a-z, A-Z, 0-9, _)
\W      - Not a Word Character
\s      - Whitespace (space, tab, newline)
\S      - Not Whitespace (space, tab, newline)

\b      - Word Boundary
\B      - Not a Word Boundary
^       - Beginning of a String
$       - End of a String

[]      - Matches Characters in brackets
[^ ]    - Matches Characters NOT in brackets
|       - Either Or
( )     - Group

Quantifiers:
*       - 0 or More
+       - 1 or More
?       - 0 or One
{3}     - Exact Number
{3,4}   - Range of Numbers (Minimum, Maximum)


Sample Regexs ###

[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+

"""
# Unix Match
"""
Sometimes you find yourself in a situation where among a huge number of files on your computer or in a separate folder you need to find files of a certain type - for example, images with the extension '.jpg' or documents with the extension '.txt', or even files that have the word 'butterfly' in their name. Doing this manually can be time-consuming. 'Matching' or patterns for searching files by a specific mask are just what you need for these sort of challenges.
This mission will help you understand how this works.

You need to find out if the given unix pattern matches the given filename.

Let me show you a couple of small examples of matching the filenames in the unix-shell. For example, * matches everything and *.txt matches all of the files that have txt extension. Here is a small table that shows symbols that can be used in patterns.

*	matches everything
?	matches any single character
[seq]	matches any character in seq
[!seq]	matches any character not in seq
Input: Two arguments. Both are strings.

Output: Bool.

Example:

unix_match('somefile.txt', '*') == True
unix_match('other.exe', '*') == True
unix_match('my.exe', '*.txt') == False
unix_match('log1.txt', 'log?.txt') == True
unix_match('log1.txt', 'log[1234567890].txt') == True
unix_match('log12.txt', 'log?.txt') == False
unix_match('log12.txt', 'log??.txt') == True
"""

import re

def unix_match3(filename: str, pattern: str) -> bool:
    
   
    pattern = pattern.replace("*", ".*").replace(".", "\\.").replace("?",".").replace("[!", "[^").replace("[]", "[^.]").replace("[^]", "\[!\]")
    print(filename)
    print(pattern)
    
    return True if re.match(r''+pattern+'', filename) != None else False