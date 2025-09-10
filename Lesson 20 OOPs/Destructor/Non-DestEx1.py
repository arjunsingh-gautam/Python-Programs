#Program for Demonstrating Destructor 
#Non-DestEx1.py
class Employee:
	def __init__(self,eno,ename):
		print("I am from Parameterised Constructor")
		self.eno=eno
		self.ename=ename
		print("Emp Num:{}".format(self.eno))
		print("Emp Name:{}".format(self.ename))
		print("-----------------------------------------------")


#Main program
print("Program Execution Started:")
e1=Employee(10,"RS") # Object Creation--Makes the PVM To call Parameterized Constructor
e2=Employee(20,"DR") # Object Creation--Makes the PVM To call Parameterized Constructor
e3=Employee(30,"TR") # Object Creation--Makes the PVM To call Parameterized Constructor
print("Program Execution Ended:")

# Default Destructor called:

""" if you do not define a custom destructor (__del__ method) in your class, Python will use the default destructor provided by the base object class. This default destructor does nothing special—it just frees the memory when the object's reference count drops to zero or when the garbage collector collects it.

So, in your code, if you do not write a __del__ method, the default destructor is called automatically when the object is deleted or goes out of scope. """