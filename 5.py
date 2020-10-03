a,b,c,d = map(int, input().split())


def horse(x1, y1, x2, y2):
    print(abs(x1-x2)), abs(y1-y2)
    print(abs(x1-x2),abs(y1-y2))
    if (abs(x1-x2)==1 and abs(y1-y2)==2):
        return ("YES")
    elif (abs(x1-x2)==2 and abs(y1-y2)==1):
        return "YES"

    else:
        return ("NO")

print(horse(int(a), int(b), int(c), int(d)))