N, K = map(int, (input().split()))
a = list()
while N+1:
    i=1
    a.append('I')
    N -= 1
while K:
    x, y = map(int, input().split())
    for i in range(x,y+1):
        if(a[i]=='I'):
            a[i]='.'
    K -= 1
a[0]=''
print(*a, sep='')
