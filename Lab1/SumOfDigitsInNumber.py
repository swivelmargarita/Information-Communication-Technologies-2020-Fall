n=int(input())
def sum( a):
    if a==0:
        return 0
    return(sum(int(a/10))+(a%10))
print(sum(n))