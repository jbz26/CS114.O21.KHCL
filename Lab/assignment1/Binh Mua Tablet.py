import math
size = int(input())
count = 0
s = size**2
t = int(math.sqrt(s/2))
for i in range(3,t,1):
  if math.sqrt(s - i**2).is_integer():
    count+=1
print(count)