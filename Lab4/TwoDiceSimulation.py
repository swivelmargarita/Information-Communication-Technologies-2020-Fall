import random
def rollDice1():
    min=1
    max=6
    return random.randint(1,6)
def rollDice2():
    return rollDice1()
statistics={
    2:0, 3:0,4:0,5:0,6:0,7:0,8:0,9:0, 10:0, 11:0,12:0
}
for i in range(0,1000):
    dice1=rollDice1()
    dice2=rollDice2()
    # print(dice1,dice2)
    index=dice1+dice2
    statistics[index]+=1
for i in range(2,13):
    statistics[i]=statistics[i]/10

print(statistics)


