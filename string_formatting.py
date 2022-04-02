# assumed order
output = "{}'s favorite number is {}".format("Kylie", 8)
print(output)

# given order
output = "{0}'s favorite number is {1}, {1} is {0}'s favorite number".format("Kylie", 8)
print(output)

# var name order
template = "{name}'s favorite number is {num}, {num} is {name}'s favorite number"
output = template.format(name="Kylie", num="8")
print(output)

# use with a frequency table like
fruit = ['orange', 'orange', 'orange', 'banana',
         'apple', 'banana', 'orange', 'banana',
         'apple', 'banana']
fruit_frequency = {}

for f in fruit:
    if f not in fruit_frequency:
        fruit_frequency[f] = 1
    else:
        fruit_frequency[f] += 1

def fruit_summary(fruit):
    num_fruit = fruit_frequency[fruit]
    output = "There are {} pieces of {} in the dataset".format(num_fruit, fruit)
    print(output)

fruit_summary("banana")

# or use it with format specifiers
print("I own {pct:.2f}% of the company".format(pct=51.3455))

print("The population of INdia is {0:,}".format(1324000000))

print("The bank balance is ${0:,.2f}".format(14558900.67890))

pop_millions = [
    ["China", 1379.302771],
    ["India", 1281.935991],
    ["USA",  326.625791],
    ["Indonesia",  260.580739],
    ["Brazil",  207.353391],
]
#some_string = "The population of {} is {0:,.2f}".format()

for pop in pop_millions:
    country = pop[0]
    population = pop[1]
    output = "The population of {} is {:,.2f} million".format(country, population)
    print(output)

# dict.items() method
for fruit, qty in fruit_freq.items():
    output = "I have {q} {f}s".format(f=fruit, q=qty)
    print(output)

