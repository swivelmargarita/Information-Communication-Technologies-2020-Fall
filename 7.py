n, m, x, y = map(int, input().split())
if m < n:
    M1 = m - x
    N1 = n - y
    ans = min([x, y, M1, N1])
    print (ans)
if n < m:
    N1 = n - x
    M1 = m - y
    ans = min([x, y, M1, N1])
    print (ans)
