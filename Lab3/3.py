s=input()
ans=str()
for i in range(0,len(s)):
    if(i==0):
        ans+=s[i].capitalize()
    else:
        ans+=s[i]
print(ans)    