import math
x1, x2, x3, x4 = map(int, input().split())


def king(x1, y1, x2, y2):
    if abs(x1-x2) <= 1 and abs(y1-y2) <= 1:
        return ("YES")
    else:
        return ("NO")

print(king(x1, x2, x3, x4))
