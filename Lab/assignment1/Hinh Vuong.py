# Đọc tọa độ điểm A từ input
a = tuple(map(int, input().split()))

# Đọc tọa độ điểm B từ input
b = tuple(map(int, input().split()))
ab = (b[0] - a[0],b[1]-a[1])
ad1 = (-ab[1],ab[0])
ad2= (ab[1],-ab[0])
d1 = (a[0]+ad1[0],a[1]+ad1[1])
d2 = (a[0] +ad2[0],a[1] +ad2[1])
c1 =( d1[0] + b[0] - a[0], d1[1]+b[1]-a[1])
c2 = ( d2[0] + b[0] - a[0], d2[1]+b[1]-a[1])
print(a,d1,c1,b);
print(a,b,c2,d2)