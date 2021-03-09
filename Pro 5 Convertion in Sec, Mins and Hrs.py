x=int(input("Enter Seconds: "))

hours= x/3600
y= x%3600
min= y/60

sec=y%60

print("Hours", hours)
print("Minutes", min)
print("Seocnds", sec)
