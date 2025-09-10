# In this code we will see instance method in Python

# In this code we will learn about instance method

class Student_info:
    course_name="Python Programming"
    def __init__(self,objinfo):
        self.objinfo=objinfo
        self.name=''
        self.prn=''

    def get_data(self):
        self.name=input(f"Enter {self.objinfo} student name:")
        self.prn=int(input(f"Enter {self.objinfo} prn no."))
        self.disp_data()
    
    def disp_data(self):
        print('-'*50)   
        print(f"{self.objinfo} Student name is:{self.name}")
        print(f"{self.objinfo} Student PRN is:{self.prn}")
        print(f"Course enrolled by {self.objinfo} Student is:{self.course_name}")
        print('-'*50)

s1=Student_info("First")
s2=Student_info("Second")
print('-'*50)
s1.get_data()
s2.get_data()
