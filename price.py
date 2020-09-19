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
discounted(1257, -24)

#задание1 версия1
def get_sum(one, two, delimiter='&'):
    label = "{a} {b} {c}".format(a=one, b=delimiter, c=two)
    return(label.upper())

s = get_sum('Python', 'Learn')
print(s)

#Задание1 версия2
def sum(one, two, delimiter='&'):
    one_two = one + delimiter + two
    return(one_two)
p = sum('python', 'learn')
print(p)

#Пример куратора
def func(x):
    return x*x

y = func(5)
print(y)

#задание2
def format_price(price):
    price = int(price)
    c = f"Цена {price} руб."
    return(c)
a = format_price(56.24)
print(a)
