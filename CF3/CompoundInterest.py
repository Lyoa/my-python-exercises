Principal = int(input("Amount deposited:"))
Interest = float(input("Annual Interest Rate:"))
Num_Years = int(input("How many years?"))

Total_Amount_of_Savings = Principal * (1 + (Interest/100)) ** Num_Years
print(format(Total_Amount_of_Savings, ".2f"))
