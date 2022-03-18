#Program to demonstarte type based dispatch

class Time:
    """Represents Time of day. 
    attributes: hour,minute,second
    """
    def __init__(self,hour=0,minute=0,second=0):
        self.hour=hour
        self.minute=minute
        self.second=second
    def __str__(self):
        return '%.2d:%.2d:%.2d' %(self.hour,self.minute,self.second)

    def __add__(self,other):
        if isinstance(other,Time):
            return  self.add_time(other)
        else:
            return self.increment(other)

    def add_time(self,other):
        sum=Time()
        sum.hour=self.hour+other.hour
        sum.minute=self.minute+other.minute
        sum.second=self.second+other.second
        if sum.second>=60:
            sum.second-=60
            sum.minute+=1
        
        if sum.minute>=60:
            sum.minute-=60
            sum.hour+=1

        return sum

    def increment(self,other):
        self.second+=other
        while self.second>=60:
            self.second-=60
            self.minute+=1
        while self.minute>=60:
            self.minute-=60
            self.hour+=1

        return self

time1=Time(9,45,35)
time2=Time(11,4,55)
print(time1+time2)    
print(time1+3450)
