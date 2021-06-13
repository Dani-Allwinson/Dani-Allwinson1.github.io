def recur_fact(n):
    if n==1:
        return n
    else:
        return n*recur_fact(n-1)

num=int(input("Enter the number:"))
if num<0:
    print("Sorry")
elif num==1:
    print("Factorial of 0 is 1")
else:
    print(recur_fact(num))