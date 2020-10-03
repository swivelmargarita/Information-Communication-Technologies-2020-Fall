box1=list(map(int,input().split()))
box2=list(map(int,input().split()))
box1.sort()
box2.sort()
a1,b1,c1=box1[0],box1[1],box1[2]
a2,b2,c2=box2[0],box2[1],box2[2]

if(a1==a2 and b1==b2 and c1==c2):
    print("Boxes are equal")
elif a1>=a2 and b1>=b2 and c1>=c2:
    print("the first box is larger than the second one")
elif a1<=a2 and b1<=b2 and c1<=c2:
    print("the first box is smaller than the second one")
else:
    print("Boxes are incomparable")
