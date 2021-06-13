#Swapping Two numbers
a=int(input("Enter the number:"))
b=int(input("Enter the number:"))
temp=0
#Swapping Condition
temp=a
a=b
b=temp
print(a)
print(b)

#Swapping Without the three variable
a=int(input("Enter the number:"))
b=int(input("Enter the number:"))
a,b=b,a
print("Swapping without Thrid number!")
print(a)
print(b)