#zoo admission price: 
# condition 1: 2 and below = 0
# condition 2: 3-12 = 14.00usd
# condition 3: 65 and above = 18.00usd
# condition4: the rest is 23.00

total = 0

while True:
    age = input("Enter ages: ")
    if age == 'end':
        break
    age = int(age) #exact
    if age <= 2: #condition 1 (babies/toddlers)
        pass
    elif age <= 12: #condition 2 (teens)
        total += 14.00
    elif age >= 65: #condition 3 (seniors)
        total += 18.00
    else: #condition 4 (the rest of guest ages)
        total += 23.00

print(f"{total:.2f}")

