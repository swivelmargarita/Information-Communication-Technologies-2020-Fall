import math
n=int(input())
a=list()
lim=1
while lim*2<=n:
    a.append(lim*2)
    lim+=lim
print(*a,end=' ')
