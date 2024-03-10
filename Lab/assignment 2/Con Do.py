l,m = map(int,input().split())
l = l*100;
left = []
right = []
for i in range(m):
  arr = input().split()
  if(arr[1]=="left"):
    left.append(int(arr[0]))
  else:
    right.append(int(arr[0]))
count = 0
first = "left";
i=0;
total = 0

while i<m:
  if(first=="left"):
    if(len(left)!=0):
      if(total+left[0]<=l):
        total+=left[0]
        left.pop(0)
        i+=1
      else:
        first ="right"
        count+=1
        total = 0
    else:
      first = "right"
      count+=1
      total = 0

    #print(i,count,total,first)
  else:
    if(first=="right"):
      if(len(right)!=0):
        if(total+right[0]<=l):
          total +=right[0]
          right.pop(0)
          i+=1
        else:
          first ="left"
          count+=1
          total = 0

      else:
        first = "left"
        count+=1
        total = 0
    #print(i,count,total,first)
print(count+1)