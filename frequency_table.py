fruit = ['orange', 'orange', 'orange', 'banana',
         'apple', 'banana', 'orange', 'banana',
         'apple', 'banana']
fruit_frequency = {}

for f in fruit:
    if f not in fruit_frequency:
        fruit_frequency[f] = 1
    else:
        fruit_frequency[f] += 1
    print(fruit_frequency)