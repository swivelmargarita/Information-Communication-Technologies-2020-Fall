s=input()
ans=str()
s=s.lower()
for i in s:
    if( i!='a' and i!='o' and i!='y' and i!='e'and  i!='u' and i!='i'):
        ans+=i
if( len(s)!=0):
    ans_fin='.'+s[0]
for i in range(1, len(ans)):
    ans_fin+='.'+ans[i]
print(ans_fin)
    
