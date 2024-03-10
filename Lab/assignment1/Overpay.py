def find(string):
  temp = ""
  for i in range(len(string)):
    if(string[i]=="%"):
      for j in range(i-1,0,-1):
        if(string[j]!=" "):
          temp = string[j]+temp;
        else:
          break
  #print(temp)
  try: float(temp)
  except: return 0
  else: return float(temp)
prices = list(map(float,input().split()))
n = len(prices)
arr = []
off = 0
onl = 0
for i in range(n) :
  arr.append(input().strip())
  temp = find(arr[i])
  onl +=prices[i];
  off = off + prices[i]/(100+temp)*100
money = float(input().strip())
if onl <=money or off<=money:
  print("true")
else:
  print("false")