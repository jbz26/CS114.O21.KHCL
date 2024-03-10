r,c = map(int,input().split())
a = [list(map(int, input().split())) for _ in range(r)]
count = 0;
for i in range(r):
  for j in range(c):
      if(a[i][j]==1):
        if(i>0):
          if(a[i-1][j]!=1):
            count+=1;
         
        else: count+=1
        if(i<r-1):
          if(a[i+1][j]!=1):
            count+=1
           
        else: count+=1
        if(j<c-1):
          if(a[i][j+1]!=1):
            count+=1
           
        else: count+=1
        if(j>0):
          if(a[i][j-1]!=1):
            count+=1
      
        else: count+=1

print(count)