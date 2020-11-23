
def toEnglish(num):
    d={
            0:"zero",1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine",10:"ten",
            11:"eleven",12:"twelve",13:"thirteen",14:"fourteen",15:"fifteen",16:"sixteen",17:"seventeen",18:"eighteen",19:"nineteen",20:"twenty",
            30:"thirty",40:"forty",50:"fifty",60:"sixty",70:"seventy",80:"eighty",90:"ninety",
            100:"one hundred",200:"two hundred",300:"three hundred",400:"four hundred",500:"five hundred",
            600:"six hundred",700:"seven hundred",800:"eight hundred",900:"nine hundred"
       }
    
    s=""
    c=0
    if(num==0):
        return "zero"
    while(num>0):
        r=num%10
        if(r!=0):
            s=d[r*(10**c)]+" "+s
        num=num//10
        c=c+1
    return s

a=int(input())
print(toEnglish(a))