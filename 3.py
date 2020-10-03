x1, x2, x3, x4 = map(int, input().split())


def elephant(x1, y1, x2, y2):
    if x1+y1==x2+y2:
        return ("YES")
    else:
        return ("NO")

print(elephant(x1, x2, x3, x4))