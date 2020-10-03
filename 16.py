a=list()
cnt=0
while True:
    n=int(input())
    if n==0:
        break
    a.append(n)
for i in range(len(a)-1):
    if a[i]<a[i+1]:
        cnt+=1
print(cnt)
