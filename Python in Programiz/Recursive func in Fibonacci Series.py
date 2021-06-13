def recursive_fib(n):
    if n<=1:
        return n
    else:
        return(recursive_fib(n-1)+ recursive_fib(n-2))

terms=int(input("Enter the number:"))

if terms<=0:
    print("Lesser than zero is not applicable")
else:
    for i in range(terms):
        print(recursive_fib(i))