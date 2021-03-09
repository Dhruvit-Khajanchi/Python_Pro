s = 'my name is dhruvit'
print("The original string is: ", s)
new_str = ""
for i in range(len(s)):
    if i != 0:
        new_str = new_str + s[i]
print(new_str)