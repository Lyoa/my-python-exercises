cents = float(input("Amount of money in cent:"))

dollars = cents//100
quarters = (cents%100)//25
dimes = ((cents % 100) % 25) // 10
nickels = (((cents % 100) % 25) % 10) // 5
pennies = ((((cents % 100) % 25) % 10) %5) // 1

print(f"{(cents*0.01)} consists of:\nDollars: {dollars:.0f}\nQuarters: {quarters:.0f}\nDimes: {dimes:.0f}\nNickels: {nickels:.0f}\nPennies: {pennies:.0f}")