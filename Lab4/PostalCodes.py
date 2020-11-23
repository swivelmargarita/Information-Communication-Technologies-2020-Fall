postalCodes={
    'A':"Newfoundland","B":"Nova Scotia","C":"Prince Edward Island","E":"New Brunswick","G":"Quebec","H":"Quebec","J":"Quebec",
    "K":"Ontario","L":"Ontario","M":"Ontario","N":"Ontario","P":"Ontario","R":"Manitoba","S":"Saskatchewan","T":"Alberta","V":"British Columbia",
    "X":"Nunavut or Northwest Territories","Y":"Yukon"
}
code=input().strip()
prov=code[0]
ans=''
ans+=str(postalCodes[prov])
if(code[1]==0):
    ans+=" and Rural"
else:
    ans+=" and Urban"
print(ans)



# print(postalCodes["J"])