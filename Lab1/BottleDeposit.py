n=int(input("1 liter, or less "))
k=int(input("Above 1 liter "))
firstTotal=n*.10
secondTotal=k*.25
total=firstTotal+secondTotal
print("{:0.2f}".format(total))


