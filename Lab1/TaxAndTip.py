n=float(input())
tip=n*.18
tax=n*.15
total=n+tip+tax
print("Tax:{:0.2f}\nTip:{:0.2f}\nTotal:{:0.2f}".format(tax,tip,total))
