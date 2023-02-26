month = input("Enter month: ")
no_days_nights = int(input("Enter the number of days or nights: "))
month = month.lower() #functionlowercase

if month == "may" or month == "october":
    deluxeP = 100 * no_days_nights
    premiumP = 85 * no_days_nights
    if no_days_nights > 14:
        deluxeP -= (deluxeP * 0.3)
        premiumP -= (premiumP * 0.1)
    elif no_days_nights > 7:
        deluxeP -= (deluxeP * 0.05)
elif month == "july" or month == "september":
    deluxeP = 112.50 * no_days_nights
    premiumP = 90.58 * no_days_nights
    if no_days_nights > 14:
        deluxeP -= (deluxeP * 0.2)
        premiumP -= (premiumP * 0.1)
elif month == "june" or month == "august":
    deluxeP = 125.66 * no_days_nights
    premiumP = 100.50 * no_days_nights
    if no_days_nights > 14:
        premiumP -= (premiumP * 0.1)

print(f'''Deluxe: {deluxeP:.2f} dollars
Premium: {premiumP:.2f} dollars''')