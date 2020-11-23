s1=input().lower().replace(" ", "")
s2=input().lower().replace(" ", "")
print(s1,s2)
s1_set=set(s1)
s2_set=set(s2)
isAnagram=True
if len(s1)==len(s2):
    for c in s1_set:
        if not(s1.count(c)==s2.count(c)):
            isAnagram=False
            break
else:
    isAnagram=False
if isAnagram:
    print("Yes")
else:
    print("not Anagram")
