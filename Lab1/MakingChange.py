#pennies1, nickels5, dimes10, quarters25, loonies100  and toonies200
n=int(input())
print(n//200,"toonies")
n=n%200
print(n//100,"loonies")
n=n%100
print(n//25, "quarters")
n = n%25
print(n//10, "dimes")
n = n%10
print(n//5, "nickles")
n = n%5
print(n//1, "pennies")

