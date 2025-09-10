# Write a python script to take the month value in numeric format and display the number of days in it.
month=int(input("Enter the month:"))
year=int(input("Enter the year:"))
if month in [1,3 ,7 ,8 ,10,12]:
    print("The month %d has 31 days"%month)
elif month==2: 
    if ((year%4==0 and year%100!=0)or(year%400==0)) :
        print("The month %d has 29 days "%month)
    else:
        print("The month %d has 28 days"%month)
else:
    print("The month %d has 30 day"%month)