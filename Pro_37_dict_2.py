price = {}
price['banana']= 4
price['apple']= 2
price['orange']= 3
price['pear']= 5
print(price['banana'])
total= 0
for k, v in price.items():
    print(k, v)
    total = total+v
print(total, "Total price")