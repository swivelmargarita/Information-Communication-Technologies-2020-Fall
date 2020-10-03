from math import sqrt
n=int(input())
if n!=0 and int(sqrt(5*(n**2)-4))**2==5*(n**2)-4 or int(sqrt(5*(n**2)+4))**2==5*(n**2)+4 :
    a = 0
    b = 1
    c = 1
    res = 0
    while (c <= n):
        res +=1#for index
        c = a + b#c for fibonacci number at f(res)
        a = b#a for copying b i.e f(res-1)
        b = c# b for copying current fibonacci number, i.e f(res) so we can add again and calculate next fib number
    print(res)
else:
    print(-1)
    

