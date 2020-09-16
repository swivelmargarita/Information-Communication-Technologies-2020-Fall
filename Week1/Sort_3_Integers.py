a = list(map(int, input().split()))
big=max(a) 
small=min(a)
medium=a[0]+a[1]+a[2]-big-small
print(small,  medium, big)