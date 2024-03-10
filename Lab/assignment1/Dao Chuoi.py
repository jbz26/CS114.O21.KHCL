n = int(input())
s1 = []
s2 = []
for i in range(n):
  s1.append(input().strip())
  s2.append(input().strip())
for i in range(n):
  if(len(s1)!=len(s2)):
    print('NO')
  else:
    countOdd = {}
    countEven = {}
    for j in range(len(s1[i])):
      if j % 2 == 1:
        if s1[i][j] in countOdd:
          countOdd[s1[i][j]] += 1
        else:
          countOdd[s1[i][j]] = 1;
      else:
        if s1[i][j] in countEven:
          countEven[s1[i][j]] += 1
        else:
          countEven[s1[i][j]]  = 1
    for j in range(len(s2[i])):
      if j % 2 == 1:
        if s2[i][j] in countOdd:
          countOdd[s2[i][j]] -= 1
        else:
          countOdd[s2[i][j]] = 1
          break
      else:
        if s2[i][j] in countEven:
          countEven[s2[i][j]] -= 1
        else:
          countEven[s2[i][j]] = 1
          break
    #print(countOdd,countEven)
    if(all(value == 0 for value in countOdd.values()) and all(value == 0 for value in countEven.values())):
      print("YES")
    else:
      print("NO")