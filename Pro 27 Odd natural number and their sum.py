start=1
sum=0
end=(int(input("Enter end range: ")))
for i in range(start,end+1):
    # print(i)
    if i%2==0:
        print(i)
        sum= sum+i
    print("Inside loop", sum)
print("Outside loop", sum)