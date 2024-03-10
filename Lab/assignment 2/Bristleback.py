n = int(input())
a = list(map(float,input().strip().split()))
x = int(input())
y = int(input())
z = float(input())
j = 0
dame = x
for i in range(1,n):
  dame+=x
  if(a[j]+z>=a[i]):
    dame +=y*(i-j)
    #print(a[j] , a[i] , dame , "!!")

  else:
    for temp in range(j,i+1):
      if(a[temp]+z>=a[i] or temp==i):
        j = temp;
        dame +=y*(i-j)
        #print(a[j] , a[i] , dame)
        break;
print(dame)