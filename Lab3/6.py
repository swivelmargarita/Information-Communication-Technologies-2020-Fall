# print(ord('A'), ord('Z'))
s=input()
ans=str()
cntUpper=0
cntLower=0
for i in range(0,len(s)):
    if(ord(s[i])<=122 and ord(s[i])>=97):
        cntLower+=1
    if(ord(s[i])<=90 and ord(s[i])>=65):
        cntUpper+=1
if(cntLower>=cntUpper):
    for i in s:
        ans+=i.lower()
else:
    for i in s:
        ans+=i.upper()
print(ans)
