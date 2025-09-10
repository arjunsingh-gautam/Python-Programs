#  Write a python script to accept one complex number from the user and display the greater number between real part and imaginary part.
complex_num=complex(input("Enter a complex number:"))
real_part=complex_num.real
imaginary_part=complex_num.imag
if real_part>imaginary_part:
    print("Real part %d is greater than Imaginary part %d"%(real_part,imaginary_part))
else:
    print("Imaginary part %d is greater than Real part %d"%(imaginary_part,real_part))