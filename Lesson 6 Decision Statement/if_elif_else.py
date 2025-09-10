""" Write a program to print grade obtained in a test . Take  marks obtained from user and display the grade
90<marks<100->A
80<marks<90->B
70<marks<80->C
60<marks<70->D
50<marks<60->E
bleow 50 ->fail"""

marks=int(input("Enter the marks to check grade:"))
if 90<marks<=100:
    print('Grade A')
elif 80<marks<=90:
    print('Grade B')
elif 70<marks<=80:
    print('Grade C')
elif 60<marks<=70:
    print('Grade D')
elif 50<marks<=60:
    print('Grade E')
elif 0<marks<=50:
    print("Fail")
else:
    print("Wrong value has been given")
