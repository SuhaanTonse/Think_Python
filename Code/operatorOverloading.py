class Book:
    def __init__(self,pages=0):
        self.pages=pages
    
    def __add__(self,other):
        return self.pages+other.pages

b1=Book(100)
b2=Book(200)

print('Total Pages :',b1+b2)