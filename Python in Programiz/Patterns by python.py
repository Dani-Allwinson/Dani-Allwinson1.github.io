"""
*
* *
* * *
* * * *
* * * * *

"""

row=int(input("Enter the rows:"))
for i in range(row):
    for j  in range(i+1):
        print("*",end=" ")
    print("\n")

"""
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
"""

row=int(input("Enter the rows:"))
for i in range(row):
    for j in range(i+1):
        print(j+1,end=" ")
    print("\n")

"""
A
B B
C C C
D D D D
E E E E E


"""

rows = int(input("Enter number of rows: "))

ascii_value = 65

for i in range(rows):
    for j in range(i+1):
        alphabet = chr(ascii_value)
        print(alphabet, end=" ")
    
    ascii_value += 1
    print("\n")

"""
* * * * *
* * * *
* * *
* *
*

"""
rows=int(input("Enter the row:"))
for i in range(row,0,-1):
    for j in range(0,i):
        print("*",end=" ")
    print("\n")

"""
1 2 3 4 5 
1 2 3 4
1 2 3
1 2 
1
"""
rows=int(input("Enter the rows:"))
for i in range(row,0,-1):
    for j in range(1,i+1):
        print(j,end=" ")
    print("\n")

"""
            *
          * * *
        * * * * *
      * * * * * * *  
"""
rows=int(input("Enter the rows:"))
k=0
for i in range(1,rows+1):
    for space in range(1,(rows-i)+1):
        print(end="  ")
    while k!=(2*i-1):
        print("*",end=" ")
        k+=1
    k=0
    print()

"""
        1
      2 3 2
    3 4 5 4 3
   4 5 6 7 5 4
 5 6 7 8 9 8 7 6 5
"""
rows = int(input("Enter number of rows: "))

k = 0
count=0
count1=0

for i in range(1, rows+1):
    for space in range(1, (rows-i)+1):
        print("  ", end="")
        count+=1
    
    while k!=((2*i)-1):
        if count<=rows-1:
            print(i+k, end=" ")
            count+=1
        else:
            count1+=1
            print(i+k-(2*count1), end=" ")
        k += 1
    
    count1 = count = k = 0
    print()

"""
  * * * * *
   * * * *
    * * *
     * *
      *
"""
rows = int(input("Enter number of rows: "))

for i in range(rows, 1, -1):
    for space in range(0, rows-i):
        print("  ", end="")
    for j in range(i, 2*i-1):
        print("* ", end="")
    for j in range(1, i-1):
        print("* ", end="")
    print()

"""
      1
    1 2 1
   1 3 3 1
  1 4 6 4 1
 1 5 10 10 5 1
PASCAL'S TRIANGLE
"""

rows = int(input("Enter number of rows: "))
coef = 1

for i in range(1, rows+1):
    for space in range(1, rows-i+1):
        print(" ",end="")
    for j in range(0, i):
        if j==0 or i==0:
            coef = 1
        else:
            coef = coef * (i - j)//j
        print(coef, end = " ")
    print()

"""
1
2 3
4 5 6
7 8 9 10

FLOYD'S TRIANGLE
"""

rows=int(input("Enter the rows:"))
num=1
for i in range(1,rows+1):
    for j in range(1,i+1):
        print(num,end=" ")
        num+=1
    print()

