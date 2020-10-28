s = input()
one = s.split("0000000")
zero = s.split("1111111")
isDangerous = False
# for i in one:
#     if len(i)>=7:
#         isDangerous=True
#         break
# print(one,zero)
if(len(one)>1 or len(zero)>1):
    print("YES")
else:
    print("NO")
