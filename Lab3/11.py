s = input()
countZ = s.count('z')
countE = s.count('e')
countR = s.count('r')
countO = s.count('o')
countN = s.count('n')
countOne = 0
countZero = 0
ans=str()
while(countO != 0 and countN != 0 and countE != 0):
    if(countO > 0 and countN > 0 and countE > 0):
        countO -= 1
        countN -= 1
        countE -= 1
        countOne += 1
while(countZ != 0 and countE != 0 and countR != 0 and countO != 0):
    if(countZ > 0 and countE > 0 and countR > 0 and countO > 0):
        countZ -= 1
        countE -= 1
        countR -= 1
        countO -= 1
        countZero += 1

while(countOne):
    ans+='1 '
    countOne-=1
while(countZero):
    ans+='0 '
    countZero-=1
print(ans.strip())

