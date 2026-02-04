x= int(input('enter no of rows'))
y= int(input('enter no of columns'))
mat=[]
print('entries row wise')
for i in range(x):
  row=[]
  for j in range(y):
    row.append(int(input()))
mat.append(row)
print('\n 2D matrix is')
for i in range(x):
  for j in range(y):
      print(mat[i][j], end=' ')
  print()

