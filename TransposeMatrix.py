import numpy as np
def traver(matrix):
  ele=[]
  for element in np.nditer(matrix):
    ele.append(element)
  return np.array(ele)
matrix=[]
m,k=list(map(int,input().split()))
for i in range(m):
  row=list(map(int,input().split()))
  matrix.append(row)
a=traver(matrix)
print(a)
