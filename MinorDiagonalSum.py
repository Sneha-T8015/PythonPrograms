import numpy as np
def solSum(matrix):
  if not matrix:
    return -1
  np_m=np.array(matrix)
  Traverse=np.fliplr(np_m)
  a=np.trace(Traverse)
  return a.tolist()
m,n=list(map(int,input().split()))
matrix=[]
for i in range(m):
  row=list(map(int,input().split()))
  matrix.append(row)
solSum(matrix)
