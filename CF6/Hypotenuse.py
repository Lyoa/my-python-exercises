def hypotenuse(side_1, side_2):
    # a^2 + b^2 = c^2 Pythagorean Theorem Formula
    # derived hypotenuse formula
	c = (side_1 ** 2 + side_2 **2) ** 0.5
	return round(c, 2)
	
print(hypotenuse(2, 5))
print(hypotenuse(15, 8))