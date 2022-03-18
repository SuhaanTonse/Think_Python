#Program to demonstarte pure functions

class Time:
    """
    Represents time of day.
    attributes: hour minutes and seconds
    """

def add_time(t1,t2):
    sum=Time()
    sum.hour=t1.hour+t2.hour
    sum.minute=t1.minute+t2.minute
    sum.second=t1.second+t2.second
    if sum.second >= 60:
        sum.second -= 60
        sum.minute += 1

    if sum.minute >= 60:
        sum.minute -= 60
        sum.hour += 1
        return sum

start=Time()
start.hour = 9
start.minute = 45
start.second = 0

duration=Time()
duration.hour = 1
duration.minute = 35
duration.second = 0

def print_time(time):
    print('%.2d:%.2d:%.2d'%(time.hour,time.minute,time.second))

done=add_time(start,duration)
print_time(done)