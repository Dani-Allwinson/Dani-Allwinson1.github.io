def recur_sumofnaturalnumber(n):
    if n<=1:
        return n
    else:
        return n + recur_sumofnaturalnumber(n-1)

num = int(input("Enter the number:"))

if num<0:
    print("None")
else:
    print(recur_sumofnaturalnumber(num))