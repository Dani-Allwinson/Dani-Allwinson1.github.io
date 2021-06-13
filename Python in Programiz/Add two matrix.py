a=[[1,2],[3,4]]
b=[[2,4],[6,8]]
c=[[0,0],[0,0]]

for i in range(len(a)):
    for j in range(len(a[0])):
        c[i][j]=a[i][j]+b[i][j]
for d in c:
    print(d)