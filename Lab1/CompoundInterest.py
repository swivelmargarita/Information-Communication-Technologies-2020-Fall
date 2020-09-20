n=float(input())
percent=.04
total=0
year=0
for i in range(3):
    year=year+1
    total=n*(1.04)**year
    print("After {:n}st year:{:.2f}".format(year,total))