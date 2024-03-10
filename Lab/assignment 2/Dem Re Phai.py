import sys
n = int(input())
a = []
v1 = None
v2 = None
count =0
for i in range(n):
  temp = list(map(int,sys.stdin.readline().split()))
  a.append(temp)
  if(i>0):
    if(i>1):
      v1 = v2
    v2 = [a[i][0]-a[i-1][0],a[i][1]-a[i-1][1]]
    #print(v1,v2)
    if(v2!=None and v1!=None):
      if(v2==[0,-1]and v1==[1,0]) or (v2==[-1,0] and v1==[0,-1]) or(v2==[0,1] and v1==[-1,0]) or(v2==[1,0] and v1==[0,1]):
        count+=1
print(count)