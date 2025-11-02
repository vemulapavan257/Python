'''Input : Number of lines : 5
Output :
 * 
* *
***
* *
* *

Input : Number of lines : 10
Output :
 **** 
*    *
*    *
*    *
*    *
******
*    *
*    *
*    *
*    *'''


n=10
m=n//2
for i in range (n):
  for j in range(m+1):
    if i==0:
      if j!=0 and j!=m:
        print('*',end='')
      else :print(' ',end='')
    elif i==m:
      print ('*',end='')
    elif j==0 or j==m:
      print ('*',end='')
    else: print (' ',end='')
    
  print() 
      
        