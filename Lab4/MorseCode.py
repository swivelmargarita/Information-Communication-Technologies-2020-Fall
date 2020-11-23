def reverseLookup(data,value): 
    keys = []
    for key in data:
        if data[key] == value:
            keys.append(key)   
    return keys
morse ={
        'A': '.-', 
        'B': '-...',
        'C': '-.-.',
        'D': '-..',
        'E': '.',
        'F': '..-.', 
        'G': '--.', 
        'H': '....',
        'I': '..', 
        'J': '.---', 
        'K': '-.-',
        'L': '.-..', 
        'M': '--', 
        'N': '-.',
        'O': '---', 
        'P': '.--.', 
        'Q': '--.-',
        'R': '.-.', 
        'S': '...', 
        'T': '-',
        'U': '..-', 
        'V': '...-', 
        'W': '.--',
        'X': '-..-', 
        'Y': '-.--', 
        'Z': '--..',
        '1': '.----', 
        '2': '..---', 
        '3': '...--',
        '4': '....-', 
        '5': '.....', 
        '6': '-....',
        '7': '--...', 
        '8': '---..', 
        '9': '----.',
        '0': '-----'
    }
a=input().split()
ans=''
for i in a:
    ans+=str(reverseLookup(morse, str(i)))
print(ans)