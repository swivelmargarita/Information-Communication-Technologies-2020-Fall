x1, x2, x3, x4 = map(int, input().split())


def queen(x1, y1, x2, y2):
    if (abs(x1-x2) <= 1 and abs(y1-y2) <= 1) or (x1==x2 or y1==y2) or (x1+y1==x2+y2):
        return ("YES")
    else:
        return ("NO")

print(queen(x1, x2, x3, x4))