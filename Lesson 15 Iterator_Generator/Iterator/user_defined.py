# In this module we will implement user defined iterator 

class MyRange:
    def __init__(self,start,end):
        self.start=start
        self.end=end

    def __iter__(self): # Every Iterator class must contain __iter__() method
        return self # it must return itself
    
    def __next__(self): # Every Iterator class must also contain __next__() method
    
    # Contains iteration logic
        if self.start>=self.end:
            raise StopIteration
        current_value=self.start
        self.start+=1
        return current_value
    
num=MyRange(1,11)

for i in num:
    print(i)