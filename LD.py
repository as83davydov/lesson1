#lists

numbers = [3, 5, 7, 9, 10.5]
numbers.append('Python')
print(numbers)
print(len(numbers))
print(numbers[0])
print(numbers[-1])
print(numbers[2:5])

numbers.remove('Python')
print(numbers)

print(numbers[0])

del numbers [0]
print(numbers)

#dictionaries

weather = {'city': 'Moskow', 'temperature': 20}
print(weather['city'])
weather['temperature'] = weather['temperature'] + 17 
print(weather['temperature'])
print(weather)

print(weather.get('country', 'Ukraine')) #ввести значение по умолчанию для ключа 'country'. если надо проверить - тоже самое без 'Ukraine'

weather['date'] = '07.09.2020'
print(weather)
print(len(weather))