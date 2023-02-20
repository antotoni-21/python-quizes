import math  
def compound_interest(p,r,t):   
    amt = p * (math.pow((1 + (r/100)),t))
    print("Compound Amount: ",amt)
    CI = amt - p
    return CI

p=float(input("Enter Principal Amount: "))
r=float(input("Enter Rate of Interest: "))
t=float(input("Enter Time Period in years: "))

print("Compound interest is" ,compound_interest(p,r,t),"%.2f")