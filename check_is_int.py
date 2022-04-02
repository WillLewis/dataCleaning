ages = []
for row in moma:
    date = row[6] # artwork year
    birth = row[3] # artists birth year
    if type(birth) == int:
        age = date - birth # age of art
    else:
        age = 0
    ages.append(age)

final_ages = []
for age in ages:
    if age > 20:
        final_age = age
    else:
        final_age = "Unknown"
    final_ages.append(final_age)

#to convert ages to a decade convert to string then strip the last digit in each age-- 86 becomes 8
# then add a "0s"
