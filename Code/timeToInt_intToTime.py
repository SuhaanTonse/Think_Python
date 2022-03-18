#Progrom to demonstrate time to int and int to time function

class Time:
    """Represents time of day.
    attributes: hour,minute,second
    """

def time_to_int(time):
    minute=time.hour*60+time.minute
    second=minute*60+time.second
    return second

def int_to_time(seconds):
    time=Time()
    minute,time.second=divmod(seconds,60)
    time.hour,time.minute=divmod(minute,60)
    return time

def increment(time,second):
    time=time_to_int(time)+second
    return int_to_time(time)

def print_time(time):
    print('%.2d:%.2d:%.2d'%(time.hour,time.minute,time.second))

time=Time()
time.hour=9
time.minute=45
time.second=35

new_time=increment(time,50)
print_time(new_time)
