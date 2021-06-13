# Check Whether the Year is Leap Year or not
# year%4==0 -->True It is a Leap Year  , year%4!=0 -->False It is not Leap Year.

Year=int(input("Enter the Year:"))
if Year%4==0:
    print("The year is Leap Year")
else:
    print("The year is not Leap Year")