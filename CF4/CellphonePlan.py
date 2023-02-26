#all charges should be in 2 decimal places except call mins and sms (float)
calls = float(input("Enter Call Air Time:"))
sms = float(input("Enter Text Messages Used:"))
#ifelif/else con
if calls > 60:
    charge_excessCalls = (calls % 60 + ((calls // 60 * 60) - 60)) * 6.50
else:
    charge_excessCalls = 0
if sms > 100:
    charge_excessSMS = (sms % 100 + ((sms // 100 * 100) - 100)) * 1
else:
    charge_excessSMS = 0

#othersurcharges
fee911 = 25
tax = (799 + charge_excessCalls + charge_excessSMS + fee911) * 0.05
total_bill = (charge_excessCalls + charge_excessSMS + fee911 + tax + 799)

#printinmulti-line
print(f'''
Call minutes: {calls:.1f}
Text messages: {sms:.1f}
Excess minute charges: {charge_excessCalls:.2f}
Excess SMS charges: {charge_excessSMS:.2f}
911 fee: {fee911:.2f}
Tax: {tax:.2f}
Total bill: {total_bill:.2f}
''')
