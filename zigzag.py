# -*- coding: utf-8 -*-
"""
automate boring stuff with Python
"""

import time, sys

indent = 0
indent_increasing = True

try :
    while True:
        print(' '*indent, end='')
        print('******')
        time.sleep(0.1) #pause for 0.1 second
         
        if indent_increasing:
            indent += 1
            if indent == 20: # change direction when reach a point
                indent_increasing = False
        else:
            indent -= 1
            if indent == 0:
                indent_increasing = True
except KeyboardInterrupt :
    sys.exit() 
    