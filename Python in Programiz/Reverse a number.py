num=1234
rev_num=0
while num!=0:
    dig=num%10
    rev_num=rev_num*10+dig
    num//=10
print(str(rev_num))