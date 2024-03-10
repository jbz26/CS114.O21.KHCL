# Mảng cần sắp xếp
arr = []
n = int(input())
for i in range(n):
  arr.append(int(input()))
# Sắp xếp mảng
arr.sort()
# In mảng sau khi sắp xếp
al = 0
for i in range(len(arr)-1):
  if(arr[i+1]-arr[i]>1):
    al += arr[i+1]-arr[i]-1
print(al)