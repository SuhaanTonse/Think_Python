#Program to demonstarte init and str method 

class Time:
    """represents time of day.
    attributes: hour,minute,second
    """
    def __init__ (self,hour=0,minute=0,second=0):
        self.hour=hour
        self.minute=minute
        self.second=second

    def __str__ (self):
        return '%.2d:%.2d:%.2d' %(self.hour,self.minute,self.second)

time=Time(9,45,35) 
print(time)