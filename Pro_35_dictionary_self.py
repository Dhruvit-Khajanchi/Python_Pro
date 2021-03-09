# dic = {'Fruit': 'Apple', 'Veg': 'Okra', 'Non-Veg': 'Chicken'}
# # for k, v in dic.items():
# #     print("Keys: ", k, " and","Values: ", v)
# # print('Fruit' not in dic.keys())
# # print("You have to bring", dic.get('Fruit'))
# dic.setdefault('Desert', 'Vanilla')
# print(dic)
message = input("Enter any Sentence: ")
count = {}
for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1