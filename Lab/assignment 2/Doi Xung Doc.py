n,m = map(int,input().split())
arr = []
for i in range(n):
  arr.append(input().strip())
for i in range(n-1,-1,-1):
  print(arr[i])