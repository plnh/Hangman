# # Lightbulb Start Watching
# """
# You have already learned how to count the amount of time a light bulb has been on, or how long a room has been lit. Now let's add one more parameter - the counting start time.

# This means that the light continues to turn on and off as before. But now, as a result of the function, I want not only to know how long there was light in the room, but how long the room was lit, starting from a certain moment.

# One more argument is added – start_watching , and if it’s not passed, we count as in the previous version of the program for the entire period.

# Input: Two arguments and only the first one is required. The first one is a list of datetime objects and the second one is a datetime object.

# Output: A number of seconds as an integer.

# Example:

# sum_light([
#     datetime(2015, 1, 12, 10, 0, 0),
#     datetime(2015, 1, 12, 10, 0, 10),
# ],
# datetime(2015, 1, 12, 10, 0, 5)) == 5

# sum_light([
#     datetime(2015, 1, 12, 10, 0, 0),
#     datetime(2015, 1, 12, 10, 0, 10),
# ], datetime(2015, 1, 12, 10, 0, 0)) == 10

# sum_light([
#     datetime(2015, 1, 12, 10, 0, 0),
#     datetime(2015, 1, 12, 10, 10, 10),
#     datetime(2015, 1, 12, 11, 0, 0),
#     datetime(2015, 1, 12, 11, 10, 10),
# ], datetime(2015, 1, 12, 11, 0, 0)) == 610
# """

# from datetime import datetime
# from typing import List

# def sum_light(els: List[datetime], start_watching: [datetime] = datetime(1, 1, 1)) -> int:
#     els = sorted(els + [start_watching])
#     count_start = els.index(start_watching)
#     result = 0
#     for i in range(count_start + (count_start % 2 == 0), len(els) ,2):
#         result += (els[i+1] - els[i]).total_seconds()
         
#     return result

# # Lightbulb End Watching
# """
# n the third mission from the series about lightbulbs, I want to separately highlight the process and the period of observation of this process.

# In the previous mission, the start_watching parameter was introduced, and in this one - the end_watching parameter, which tells the time when it’s necessary to end the observation. If it’s not passed, the mission works as in the previous version, with no observation time limit.

# One more update is that the amount of elements (button clicks) can be odd (previously there was a precondition, that the amount of elements is always even).
# Input: Three arguments and only the first one is required. The first one is a list of datetime objects, the second and the third ones are the datetime objects.

# Output: A number of seconds as an integer.

# Example:

# sum_light([
#     datetime(2015, 1, 12, 10, 0, 0),
#     datetime(2015, 1, 12, 10, 10, 10),
#     datetime(2015, 1, 12, 11, 0, 0),
# ],
# datetime(2015, 1, 12, 10, 10, 0),
# datetime(2015, 1, 12, 11, 0, 10)) == 20

# sum_light([
#     datetime(2015, 1, 12, 10, 0, 0),
# ],
# datetime(2015, 1, 12, 9, 9, 0),
# datetime(2015, 1, 12, 10, 0, 0)) == 0

# sum_light([
#     datetime(2015, 1, 12, 10, 0, 0),
#     datetime(2015, 1, 12, 10, 10, 10),
#     datetime(2015, 1, 12, 11, 0, 0),
#     datetime(2015, 1, 12, 11, 10, 10),
# ],
# datetime(2015, 1, 12, 9, 0, 0),
# datetime(2015, 1, 12, 10, 5, 0)) == 300
# """

# from datetime import datetime
# from typing import List

# def sum_light(els: List[datetime], start_watching: [datetime] = datetime(1, 1, 1), end_watching: [datetime] = datetime(9999,12,31)) -> int:
#     els = sorted(els + [start_watching] +[end_watching])
#     count_start = els.index(start_watching)
#     count_stop = els.index(end_watching)
#     result = 0
#     for i in range(count_start + (count_start % 2 == 0), count_stop,2):
#         result += (els[i+1] - els[i]).total_seconds()
         
#     return result

# # Multiple Lightbulbs
# """
# In the 4th mission of the series more light bulbs are added.

# You still must determine how long the room will be lit during the observation period between start_watching and end_watching. But now we have more than one light bulb. This means that in the light bulb switching array can now also be passed the number of the light bulb, the button of which is being pressed.

# Each element of the button clicking array can be either a datetime object (which means the time when the first button was pressed) or a tuple of 2 elements (where the first elements is a datetime object, the time the button was pressed), and the second is the number of the light bulb, the button of which is being pressed.

# If the passed array will only consist of datetime elements, then we have only one light bulb and the function should work the same way as in the previous mission of the series.

# Input: Three arguments and only the first one is required. The first one is a list of datetime objects (instead of datetime object there can be a tuple of two datetime and int), the second and the third ones are the datetime objects.

# Output: A number of seconds as an integer.

# Example:

# sum_light([
#     datetime(2015, 1, 12, 10, 0, 0),
#     datetime(2015, 1, 12, 10, 0, 10),
#     (datetime(2015, 1, 12, 10, 0, 0), 2),
#     (datetime(2015, 1, 12, 10, 1, 0), 2),
# ]) == 60

# sum_light([
#     (datetime(2015, 1, 12, 10, 0, 10), 3),
#     datetime(2015, 1, 12, 10, 0, 20),
#     (datetime(2015, 1, 12, 10, 0, 30), 3),
#     (datetime(2015, 1, 12, 10, 0, 30), 2),
#     datetime(2015, 1, 12, 10, 0, 40),
#     (datetime(2015, 1, 12, 10, 0, 50), 2),
#     (datetime(2015, 1, 12, 10, 1, 0), 3),
#     (datetime(2015, 1, 12, 10, 1, 20), 3),
# ]) == 60

# sum_light([
#     datetime(2015, 1, 12, 10, 0, 20),
#     (datetime(2015, 1, 12, 10, 0, 30), 2),
#     datetime(2015, 1, 12, 10, 0, 40),
#     (datetime(2015, 1, 12, 10, 0, 50), 2),
# ], datetime(2015, 1, 12, 10, 0, 30)) == 20

# sum_light([
#     datetime(2015, 1, 12, 10, 0, 0),
#     datetime(2015, 1, 12, 10, 0, 10),
#     (datetime(2015, 1, 12, 10, 0, 0), 2),
#     (datetime(2015, 1, 12, 10, 1, 0), 2),
# ], datetime(2015, 1, 12, 10, 0, 20), datetime(2015, 1, 12, 10, 1, 0)) == 40

# """

# from datetime import datetime
# from typing import List



    
# def sum_light(els, start_watching: [datetime] = datetime(1, 1, 1), end_watching: [datetime] = datetime(9999,12,31)) -> int:
    
#     button_pressed = []
#     for i in els:
#         if type(i) == tuple:
#             button_pressed.append(i)
#         else:
#             button_pressed.append((i,1))
#     button_pressed.sort() 
    
#     if len(button_pressed) % 2 == 1:
#         button_pressed.append((end_watching,0))
   
#     result = 0
#     time_stamp = None
#     light_on = set()
#     for x,y in button_pressed:
#         if len(light_on) > 0:
#             temp = ( min(end_watching, x) - max(start_watching, time_stamp)).total_seconds()
#             if temp > 0:
#                 result += temp
                
#         if y not in light_on:
#             light_on.add(y)
#         else:
#             light_on.remove(y)
            
#         time_stamp = x
        
#     return result

