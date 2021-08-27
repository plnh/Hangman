# # Lightbulb Operating
# """
# Since you are here, it means that you’ve already solved 4 missions of the series. Your function can already adopt more than one light bulb in the date array to determine if the room is lit or not. And with the second and third elements the period we want to observe can be defined.

# In the 5th mission, a fourth argument is added - the operating time of the light bulbs. By analogy with the previous missions - if it’s not passed, then the bulb works indefinitely.

# The operating time argument is passed as a timedelta object. It shows how long the light bulb can work when it’s on. It has no cooling, which means that if our bulb can work for only one hour, then it can work for 30 minutes now and 30 minutes next year. After that it will turn itself off and will no longer respond to the button.

# We still need to calculate how long the room has been lit.
# Input: Four arguments and only the first one is required. The first one (els) is a list of datetime objects (instead of datetime object there can be a tuple of two datetime and int), the second (start_watching) and the third ones (end_watching) is the datetime objects. The forth argument (operating) - timedelta object - how long the lamp can work.

# Output: A number of seconds as an integer.

# Example:

# sum_light([
#     datetime(2015, 1, 12, 10, 0, 0),
#     datetime(2015, 1, 12, 10, 0, 30),
#     (datetime(2015, 1, 12, 10, 0, 30), 2),
#     (datetime(2015, 1, 12, 10, 1, 0), 2),
# ], operating=timedelta(seconds=20)) == 40

# sum_light([
#     (datetime(2015, 1, 12, 10, 0, 10), 3),
#     datetime(2015, 1, 12, 10, 0, 20),
#     (datetime(2015, 1, 12, 10, 0, 30), 3),
#     (datetime(2015, 1, 12, 10, 0, 30), 2),
#     datetime(2015, 1, 12, 10, 0, 40),
#     (datetime(2015, 1, 12, 10, 0, 50), 2),
#     (datetime(2015, 1, 12, 10, 1, 20), 2),
#     (datetime(2015, 1, 12, 10, 1, 40), 2),
# ], start_watching=datetime(2015, 1, 12, 10, 0, 20), operating=timedelta(seconds=100)) == 50

# sum_light([
#     (datetime(2015, 1, 12, 10, 0, 10), 3),
#     datetime(2015, 1, 12, 10, 0, 20),
#     (datetime(2015, 1, 12, 10, 0, 30), 3),
#     (datetime(2015, 1, 12, 10, 0, 30), 2),
# ], 
# start_watching=datetime(2015, 1, 12, 10, 0, 10),
# end_watching=datetime(2015, 1, 12, 10, 0, 30),
# operating=timedelta(seconds=5)) == 10
# """

# from datetime import datetime, timedelta
# , Optional, Union, Tuple
# from pprint import pprint


# def sum_light(els: List[Union[datetime, Tuple[datetime, int]]], start_watching: [datetime] = datetime(1970, 1, 1), end_watching: [datetime] = datetime(9999,12,31), operating: Optional[timedelta] = None) -> int:
# #set start_watchin and end_watchin to min and max availble 
    
#     # Unify els element into (datetime: datetime[], lamp number: int)
#     els_add_lamp_number = []
#     for i in els:
#         if not isinstance(i,tuple) and not isinstance(i, list):
#             temp_list = [i,1]
#             els_add_lamp_number.append(tuple(temp_list))
#         else:
#             els_add_lamp_number.append(tuple(i))
#     els = sorted(els_add_lamp_number)
    
#     # sort time stamp (on,off) into group if lamp number
#     # create a dict{ lapnumber: list[(on,off)]}
#     light_on = []
#     on_off = {}
#     for time, lamp_number in els:
#         if lamp_number not in light_on:
#             light_on.append(lamp_number) # create key: lamp_number
#             #add on time stamp
#             if on_off.get(lamp_number) == None:  
#                 on_off[lamp_number] = [[time, ]] 
#             else:
#                 on_off[lamp_number].append([time, ])
#         # add off time stamp into the tuple
#         else: 
#             light_on.remove(lamp_number)
#             on_off[lamp_number][-1].append(time)
    
#     on_off_operating = {}
#     #update off time stamp with operation time
#     if operating != None: #take into account operation time
#         for lamp_number in on_off.keys():
#             time_used = 0
#             time_left = operating
                       
#             for time in on_off[lamp_number]:
                
#                 if len(time) % 2 == 1:
#                     time.append(datetime(9999, 12, 31, 0, 0, 0))
                    
#                 time_used += (time[1] - time[0]).total_seconds() #calculte how long the lamp is on
#                 if time_used <= time_left.seconds:
#                     if on_off_operating.get(lamp_number) == None: # create new key and add List[time on, time off]
#                         on_off_operating[lamp_number] = [[time[0], time[1]], ] #make sure use [ [], ] to enable adding another list
#                     else:
#                         on_off_operating[lamp_number].append([time[0], time[1]]) #don't use [ [], ] as it'll create double list
#                     time_left -= (time[1] - time[0])
#                 else:
#                     if on_off_operating.get(lamp_number) == None:
#                         on_off_operating[lamp_number] = [[time[0], time[0] + time_left], ] #see above
#                         break
#                     else:
#                         on_off_operating[lamp_number].append([time[0], time[0] + time_left]) #see above
#                         break
           
#         els_temp = []
#         # reformat on_off_operating to simple list with tuple(datetime, lamp_number)
#         # output list of (timestamp, lampnumber) considering operation time         
#         for lamp_number in on_off_operating.keys():
                        
#             for time in range(len(on_off_operating[lamp_number])):
                                
#                 els_temp.append(tuple([on_off_operating[lamp_number][time][0], lamp_number]))
#                 els_temp.append(tuple([on_off_operating[lamp_number][time][1], lamp_number]))
                
#         els = sorted(els_temp) #output
        
#     # make sure len(els) is even
#     if len(els) % 2 == 1:
#         els.append((end_watching,0))
    
#     #calculte duration of light on
#     result = 0
#     time_stamp = None
#     all_light_on = set()
    
#     for time, lamp_number in els:
#         if len(all_light_on) > 0: #if len == 0 all light is off and no calculation
#             temp = ( min(time,end_watching) - max(time_stamp, start_watching)).total_seconds() #take into account start and end time
#             if int(temp) > 0:
#                 result += temp
                
#         if lamp_number not in all_light_on: #update which light is on
#             all_light_on.add(lamp_number) 
#         else:
#             all_light_on.remove(lamp_number)
            
#         time_stamp = time #update time stamp
        
        
#     return result

# Lightbulb More
"""
The complication in the 6th mission of the series is that now there might be needed more than one light bulb to illuminate a room. And this is the 5th argument of the function - how many light bulbs are needed to illuminate the room.

For example, if you need 3 bulbs to illuminate a room, then we don’t count the time when there were only 2 bulbs or only one. If the last argument of the function is not passed, then one light bulb is enough to illuminate the room.

The task is still the same - to find out how long the room was lit (in this task, we can say - sufficiently lit).

example

Input: Five arguments and only the first one is required. The first one (els) is a list of datetime objects (instead of datetime object there can be a tuple of two datetime and int), the second (start_watching) and the third ones (end_watching) are the datetime objects. The forth argument (operating) - timedelta object - how long the lamp can work. The 5th argument is a positive non-zero int.

Output: A number of seconds as an integer.

Example:

sum_light([
    (datetime(2015, 1, 12, 10, 0, 10), 3),
    datetime(2015, 1, 12, 10, 0, 20),
    (datetime(2015, 1, 12, 10, 0, 30), 3),
    (datetime(2015, 1, 12, 10, 0, 30), 2),
    datetime(2015, 1, 12, 10, 0, 40),
    (datetime(2015, 1, 12, 10, 0, 50), 2),
], req=2) == 20

sum_light([
    (datetime(2015, 1, 12, 10, 0, 10), 3),
    datetime(2015, 1, 12, 10, 0, 20),
    (datetime(2015, 1, 12, 10, 0, 30), 3),
    (datetime(2015, 1, 12, 10, 0, 30), 2),
    datetime(2015, 1, 12, 10, 0, 40),
    (datetime(2015, 1, 12, 10, 0, 50), 2),
], req=3) == 0

sum_light([
    (datetime(2015, 1, 12, 10, 0, 10), 3),
    datetime(2015, 1, 12, 10, 0, 20),
    (datetime(2015, 1, 12, 10, 0, 30), 2),
    (datetime(2015, 1, 12, 10, 0, 50), 3),
    datetime(2015, 1, 12, 10, 0, 40),
    (datetime(2015, 1, 12, 10, 0, 50), 2),
], req=3) == 10
"""

from datetime import datetime, timedelta
from typing import List, Optional, Union, Tuple
from pprint import pprint


def sum_light(els: List[Union[datetime, Tuple[datetime, int]]], 
          start_watching: Optional[datetime] = datetime(1970, 1, 1), 
          end_watching: Optional[datetime] = datetime(9999, 12, 31), 
          operating: Optional[timedelta] = None, 
          req: Optional[int] = 1):
#set start_watchin and end_watchin to min and max availble 
    
    # Unify els element into (datetime: datetime[], lamp number: int)
    els_add_lamp_number = []
    for i in els:
        if not isinstance(i,tuple) and not isinstance(i, list):
            temp_list = [i,1]
            els_add_lamp_number.append(tuple(temp_list))
        else:
            els_add_lamp_number.append(tuple(i))
    els = sorted(els_add_lamp_number)
    
    # sort time stamp (on,off) into group if lamp number
    # create a dict{ lapnumber: list[(on,off)]}
    light_on = []
    on_off = {}
    for time, lamp_number in els:
        if lamp_number not in light_on:
            light_on.append(lamp_number) # create key: lamp_number
            #add on time stamp
            if on_off.get(lamp_number) == None:  
                on_off[lamp_number] = [[time, ]] 
            else:
                on_off[lamp_number].append([time, ])
        # add off time stamp into the tuple
        else: 
            light_on.remove(lamp_number)
            on_off[lamp_number][-1].append(time)
    
    on_off_operating = {}
    #update off time stamp with operation time
    if operating != None: #take into account operation time
        for lamp_number in on_off.keys():
            time_used = 0
            time_left = operating
                       
            for time in on_off[lamp_number]:
                
                if len(time) % 2 == 1:
                    time.append(datetime(9999, 12, 31, 0, 0, 0))
                    
                time_used += (time[1] - time[0]).total_seconds() #calculte how long the lamp is on
                if time_used <= time_left.seconds:
                    if on_off_operating.get(lamp_number) == None: # create new key and add List[time on, time off]
                        on_off_operating[lamp_number] = [[time[0], time[1]], ] #make sure use [ [], ] to enable adding another list
                    else:
                        on_off_operating[lamp_number].append([time[0], time[1]]) #don't use [ [], ] as it'll create double list
                    time_left -= (time[1] - time[0])
                else:
                    if on_off_operating.get(lamp_number) == None:
                        on_off_operating[lamp_number] = [[time[0], time[0] + time_left], ] #see above
                        break
                    else:
                        on_off_operating[lamp_number].append([time[0], time[0] + time_left]) #see above
                        break
           
        els_temp = []
        # reformat on_off_operating to simple list with tuple(datetime, lamp_number)
        # output list of (timestamp, lampnumber) considering operation time         
        for lamp_number in on_off_operating.keys():
                        
            for time in range(len(on_off_operating[lamp_number])):
                                
                els_temp.append(tuple([on_off_operating[lamp_number][time][0], lamp_number]))
                els_temp.append(tuple([on_off_operating[lamp_number][time][1], lamp_number]))
                
        els = sorted(els_temp) #output
        
    # make sure len(els) is even
    if len(els) % 2 == 1:
        els.append((end_watching,0))
    
    #calculte duration of light on
    result = 0
    time_stamp = None
    all_light_on = set()
    
    n = 0
    for time, lamp_number in els:
                
        if len(all_light_on) >= req: 
            temp = ( min(time,end_watching) - max(time_stamp, start_watching) ).total_seconds() #take into account start and end time
            
            if int(temp) > 0:
                result += temp
                
        if lamp_number not in all_light_on: #update which light is on
            all_light_on.add(lamp_number) 
        else:
            all_light_on.remove(lamp_number)
            
        time_stamp = time #update time stamp
        
        
    return result


