a=1234
reverse = 0
while a>0:
    x=a%10
    reverse = reverse*10 + x
    a=a//10
print(reverse)

