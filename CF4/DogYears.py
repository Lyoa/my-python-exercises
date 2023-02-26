HumanYears = int(input("Human Years: "))

if HumanYears <= 2:
    dogAge = (HumanYears - 2) * 10.5
else:
    dogAge = (HumanYears - 2) * 4 + 21

print(dogAge)