'''Input : row = 7, column = 7        
Output:
*     * * * *
*     *
*     *
* * * * * * *
      *     *
      *     *
* * * *     *

Input : row = 11, column = 11
Output :
*         * * * * * *
*         *
*         *
*         *
*         *
* * * * * * * * * * * 
          *         * 
          *         * 
          *         * 
          *         * 
* * * * * *         * '''


n=15
m=n//2
for i in range (n):
  for j in range (n):
    if i==m or j==m:
      print('*',end='')
    elif i==0 and j>=m:
      print('*',end='')
    elif j==0 and i<=m:
      print('*',end='')
    elif i==n-1 and j<=m:
      print('*',end='') 
    elif j==n-1 and i>=m:
      print('*',end='')              
    else: print(' ',end='')
  print()