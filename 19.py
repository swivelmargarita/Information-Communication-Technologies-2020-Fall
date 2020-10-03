from math import factorial
n=int(input())
a=list(map(int,input().split()))
aSet=list(set(a))
cnt=0
for i in range(len(aSet)):
    if a.count(aSet[i])>=2:
        cnt+=(factorial(a.count(aSet[i]))/(factorial(2)*factorial(a.count(aSet[i])-2)))
print(int(cnt))
