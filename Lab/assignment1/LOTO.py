metric = []
for i in range(3):
  a = list(map(int,(input().strip().split())))
  metric.append(a)
n = int(input())
for i in range(n):
  temp = int(input())
  for i in range(3):
    if(temp in metric[i]):
      metric[i][metric[i].index(temp)] = -1;
cheo1=0
cheo2=0
for i in range(3):
  if(sum(metric[i])==-3):
    print("Yes")
    exit()
  if(metric[0][i] + metric[1][i]+metric[2][i] == -3):
    print("Yes")
    exit()
  cheo1 = cheo1+metric[i][i]
  cheo2 = cheo2+ metric[i][2-i]
if(cheo1==-3 or cheo2==-3):
  print("Yes")
  exit()
print("No")