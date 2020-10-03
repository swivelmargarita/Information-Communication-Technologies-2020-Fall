n,m,k=map(int,input().split())
if ((k%n==0 and n*m>k) or (n*m>k and k%m==0)) :
    print("YES")
else:
    print("NO")