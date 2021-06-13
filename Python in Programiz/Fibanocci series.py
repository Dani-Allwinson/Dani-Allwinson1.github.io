terms=int(input("Enter the number of terms:"))
num1=int(input("Enter the 1st number:"))
num2=int(input("Enter the 2nd number:"))
if terms==1:
    print(num1)
else:
    print(num1)
    print(num2)
    for i in range(2,terms):
        num3=num1+num2
        num1=num2
        num2=num3
        print(num3)