def prime_number(num):
    a = False
    if num > 1:
    
     for i in range(2, num):
        if (num % i) == 0:
            
            a = True
            
            break
    if a:
        print(num, "is not a prime number")
    else:
        print(num, "is a prime number")

prime_number(5)



    