n=8
print("Solid Square:")
for i in range (n):
  for j in range(n):
    print('*',end='')
  print()
print("Hollow Square:")
for i in range (n):
  for j in range(n):
    if i==0 or i==n-1 or j==0 or j==n-1:
      print('*',end='')
    else :print(' ',end='')
      
  print()