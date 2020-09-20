#program that reads a duration from the user as a number of days, hours, minutes, and seconds
#total number of seconds represented by this duration
d=int(input())
h=int(input())
s=int(input())
print(d*24*60*60+h*60*60+s)
