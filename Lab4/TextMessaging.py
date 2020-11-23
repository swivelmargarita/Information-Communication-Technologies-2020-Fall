numbers = {
    1:['.',',','?','!',':'],
    2:['A' ,'B','C'],
    3:['D' ,'E','F' ],
    4:['G' ,'H' ,'I' ],
    5:['J' ,'K' ,'L' ],
    6:['M' ,'N' ,'O'],
    7:['P' ,'Q' ,'R' ,'S'],
    8:['T' ,'U' ,'V' ],
    9:['W' ,'X' ,'Y' ,'Z' ],
    0:[' '] 
    }
s=input()
s_set=''
for c in s:
    # print(c)
    if s_set.count(c)==0:
        s_set+=c
# print(s_set)
ans=''
for i in s_set:
    ans+=numbers[int(i)][(s.count(i)-1)%len(numbers[int(i)])]
    # print(ans)
print(ans)