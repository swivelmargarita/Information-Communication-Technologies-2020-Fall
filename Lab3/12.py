s=input()
# print(s)
cnt=0
ans=0
for i in s:
    if(i=="x"):#If string is full of x's keep increasing the counter and find the answer afterthe loop 
        cnt+=1
    else:
        maxXBiggerThan2=cnt-2#While iterating, if we found char other than 'x' then:
                             # 1) if there's no mo than 2 x's max allways will be 0
                             #2)if more than 2 x's since 2 x's is permissible save the count of to be deleted an add to ans
        ans+=max(0,maxXBiggerThan2)
        cnt=0#After that reset the counter, because previous strike was over.
maxXBiggerThan2=cnt-2
ans=max(0,maxXBiggerThan2)
print(ans)