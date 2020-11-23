def reverseLookup(data,value): 
    keys = []
    for key in data:
        if data[key] == value:
            keys.append(key)   
    return keys
myDic={
    "color":"red",
    "price":"pricey",
    "brand":"ferrari",
    "model":"488",
    "watch":"pricey"
}
print(reverseLookup(myDic, "red"))
print(reverseLookup(myDic, "488"))
print(reverseLookup(myDic, "pricey"))



