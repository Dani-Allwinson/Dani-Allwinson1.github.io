num=int(input("Enter the number:"))
if num>1:
    for i in range(2,num):
        if num%i==0:
            print("It is not a prime number.")
            break
    else:
        print("It is a prime number.")
else:
    print("1 is not a prime number")


# Defining a function
def prime(num):
    if num>1:
        for i in range(2,num):
            if num%i==0:
                print("It is not a prime number")
                break
        else:
            print("It is a prime number")
    else:
        print("1 is not a prime number")
print("Define in function")
prime(7)