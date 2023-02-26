month = int(input("Month: "))

if month == 2:
    print("28 or 29 days")
elif month in [4, 6, 9, 11]:
    print("30 days")
else:
    print("31 days")