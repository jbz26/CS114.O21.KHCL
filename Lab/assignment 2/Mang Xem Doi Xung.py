import sys
n = int(input())
if(n>=1):
  a = []
  for _ in range(n):
      a.append(int(sys.stdin.readline()))
  count = 0
  #print(a)
  for i in range(int(n/2)):
    if(a[i]!=a[n-1-i]):
      count+=1
  if(count>1):
        print("FALSE")
        exit()
  print("TRUE")