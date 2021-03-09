s = input("Enter any String: ")
s2 = s.capitalize()
print(s2)
s2 = s.lower()
print(s2)
s2 = s.upper()
print(s2)
s2 = s.title()
print(s2)
s2 = s2.lower()
print(s2)
alpha_count = 0
numeric_count = 0
space_count = 0
for character in s2:
    if character.isalpha():
        alpha_count = alpha_count+1
    elif character.isnumeric():
        numeric_count = numeric_count+1
    elif character.isspace():
        space_count = space_count+1
print("number of characters: ", alpha_count)
print("number of numerics: ", numeric_count)
print("number of spaces: ", space_count)
vowel = ['a', 'e', 'i', 'o', 'u']
vowel_count = 0
for character in vowel:
    vowel_count = vowel_count + s2.count(character)
print('numbers of vowels in string: ', vowel_count)