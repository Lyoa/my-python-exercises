# amount = 2000
# tax = (amount * 0.12)
# emergency_fund = (amount - tax) * 0.10
# stay = (amount - tax) - emergency_fund

# print("Tax:", end=' ') ;print('%.2f' % tax)
# print("Emergency Fund:", end=' ') ;print('%.2f' % emergency_fund)
# print("Accomodation:", end=' ') ;print('%.2f' % stay)

amount = float(input("Amount paid by the user:"))

tax = amount * 0.12
emergency_fund = (amount-tax) * 0.1
stay = (amount-tax) - emergency_fund
print(f'Tax: {tax:.2f}\nEmergency Fund: {emergency_fund:.2f}\nAccomodation: {stay:.2f}')

# amount = float(input("Amount paid by the user:"))

# tax = amount * 0.12
# emergency_fund = (amount - tax) * 0.1
# stay = (amount - tax) - emergency_fund
# print(f'Tax: {tax:.2f}\nEmergency Fund: {emergency_fund:.2f}\nAccommodation: {stay:.2f}')