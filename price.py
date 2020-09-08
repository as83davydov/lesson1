#price = 100
#discount = 5

#price_with_discount = price - price * discount / 100

#print(price_with_discount)

def discounted(price, discount):
    price = abs(float(price)) #нужно делаь проверку на исключения
    discount = abs(float(discount))
    if discount >= 100:
        price_with_discount = price
    else:
        price_with_discount = price - price * discount / 100
    print(price_with_discount)

discounted(234, 101)
discounted(200, 30)
discounted(-500, -30)