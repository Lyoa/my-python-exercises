BookPrice = 24.95
Discount = 24.95 * 0.4
Shipping = 3.00
Shipping2 = 0.75

Quantity = float(input("Book purchased:"))
Fbookprice = BookPrice - Discount
Sbookprice = Fbookprice + Shipping2
AllBooks = ( Fbookprice + Shipping ) + ((Quantity - 1) * Sbookprice)
print(f"{AllBooks:.2f}")