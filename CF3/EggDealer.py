Quantity_Egg = int(input("Number of eggs purchased:"))
Price_Egg = (Quantity_Egg//12 * 70) + (Quantity_Egg%12 * 7)
print(Price_Egg)