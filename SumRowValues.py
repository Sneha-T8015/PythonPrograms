import numpy as np
def solSum(matrix):
  if not matrix:
    return -1
  np_m=np.array(matrix)
  a=np.sum(np_m,axis=1)
  return a.tolist()
m,n=list(map(int,input().split()))
matrix=[]
for i in range(m):
  row=list(map(int,input().split()))
  matrix.append(row)
solSum(matrix)
