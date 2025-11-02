'''
123454321
2       2
3       3
4       4
5       5
4       4
3       3
2       2
123454321
'''
m=5
n=m*2
for i in range (n-1):
    for j in range (n-1):
        data=i+j+1
        if i+j>=m and i+j<=n-2:
            data=n-(i+j)-1
        if i+j>=n-2:
            data= ((i+j)+1)-(n-2)
            if data>=m:
                data=n-data
        if i==0 or i==n-2:
            print(data ,end='')
        elif j==0 or j==n-2:
            print(data,end='')       
        else:print(' ',end='')
    print()