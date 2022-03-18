#Program to print time

class Time:
    """Represents the  time of day.
    attributes: hour,minute,second
    """

time=Time()
time.hour=9
time.minute=45
time.second=52

def print_time(time):
    print('%.2d:%.2d:%.2d'%(time.hour,time.minute,time.second))

print_time(time)