def isLower(c):
    if(ord(c)<=122 and ord(c)>=97):
        return True
def isUpper(c):
    if(ord(c)<=90 and ord(c)>=65):
        return True
s=input()
cntUpper=0
cntLower=0
ans=str()
for i in range(0,len(s)):
    if(ord(s[i])<=122 and ord(s[i])>=97):
        cntLower+=1
    if(ord(s[i])<=90 and ord(s[i])>=65):
        cntUpper+=1
if(isLower(s[0])):
    # print(cntLower, cntUpper)
    if(cntUpper+1==len(s)):
        for i in range(0,len(s)):
            if(i==0):
                ans+=s[i].upper()
            else:
                ans+=s[i].lower()
elif(len(s)==1 and cntLower==1):
    ans+=s[0].upper()
elif(len(s)==cntUpper):
    for i in range(0,len(s)):
        ans+=s[i].lower()

print(ans)