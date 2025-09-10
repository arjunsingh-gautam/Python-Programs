l1=[2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]

def Primenum(n): # This function helps fiter to filter out prime numbers from l1 list
    for i in range(2,n):
        if n%i==0:
            return False
    return True


f=list(filter(Primenum,l1)) 
print("The prime number in list l1 is:",f)

