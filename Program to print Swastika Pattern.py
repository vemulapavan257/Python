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


n=7
for i in range (n):
    for j in range (n):
        if i==(n//2):
            print('1',end='')
        elif j==(n//2):
            print('2',end='')
        elif j==0 and i<= n//2:
            print('3',end='')
        elif i>= n//2 and j==n:
            print('4',end='')
        else :
            print(" ",end ="")
    print()
