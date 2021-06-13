Start=int(input("Enter the starting number:"))
End=int(input("Enter the Ending number:"))

for num in range(Start,End+1):
    if num>1:
        for i in range(2,num):   
            if num%i==0:
                break
        else:
            print(num)

    