a=list()
while True:
    n=int(input())
    a.append(n)
    if n==0:
        print(a.count(max(a)))
        break