# endless generator:

def fib():
  a,b=0,1
  while True: 
    yield a
    a,b=b,a+b

it=fib()
fib_list=[]
while True:
  ans=input("Enter y/n to generat a fibonacci number:")
  if ans=='y':
    x=next(it)
    print(x)
    fib_list.append(x)
  else:
    print("The list of fibonacci numbers generated:",fib_list)
    break