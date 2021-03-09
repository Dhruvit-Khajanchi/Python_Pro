p=int(input("Enter Principle: "))
r=int(input("Enter Rate: "))
t=int(input("Enter Time: "))
ci= p*(1+r/100)**t - p
print("Compound Interest =", ci)