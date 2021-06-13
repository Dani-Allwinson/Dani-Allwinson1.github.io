my_str="aIbohPhoBiA"
my_str= my_str.casefold()
rev_str=reversed(my_str)
if list(my_str)==list(rev_str):
    print("It is a polindrome")
else:
    print("It is not a palindrome")

num=121

temp=num
rev=0
while(num>0):
    dig=num%10
    rev=rev*10+dig
    num=num//10
if(temp==rev):
    print("The number is palindrome!")
else:
    print("Not a palindrome!")