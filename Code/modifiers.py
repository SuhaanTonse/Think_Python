#Program to demonstrate modifiers

class Time:
    """Represents time of day.
    attributes: hour,minute,second
    """

def increment_time(time,second):
    time.second+=second

    if time.second>=60:
        time.second-=60
        time.minute+=1

    if time.minute>=60:
        time.minute-=60
        time.hour+=1
    
    return time

def print_time(time):
    print('%.2d:%.2d:%.2d'%(time.hour,time.minute,time.second))

time=Time()
time.hour=9
time.minute=45
time.second=35

newtime=increment_time(time,500)
print_time(newtime)
