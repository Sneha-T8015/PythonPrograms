def getAntiDiagonals(matrix):
  n=len(matrix)
  l=2*n-1
  antiD=[[0] for _ in range(l)]
  for i in range(n):
    for j in range(n):
      antiD[i+j].append(matrix[i][j])
  return antiD
matrix=[]
m,k=list(map(int,input().split()))
for i in range(m):
  row=list(map(int,input().split()))
  matrix.append(row)
getAntiDiagonals(matrix)
