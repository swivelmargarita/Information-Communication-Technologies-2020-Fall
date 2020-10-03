import math
n=int(input())
a=list()
lim=1
while lim*lim<=n:
    a.append(lim*lim)
    lim+=1
print(*a,end=' ')
