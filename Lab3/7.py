s=input()
s_set=set()
for i in s:
    if((ord(i)<=122 and ord(i)>=97) or (ord(i)<=90 and ord(i)>=65)):
        s_set.add(i.lower())
print(s_set)
if(len(s_set)==26):
    print("YES")
else:
    print("NO")
