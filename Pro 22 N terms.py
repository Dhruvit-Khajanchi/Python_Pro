start = 1
end = int(input("Enter Number: "))
sum=0
while start <= end:
    print(start, end=" ")
    sum = sum + start
    start = start+1
print("\n", sum)