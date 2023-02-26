class Car:
    def __init__(self, brand_name, kilometers, liters):
        self.brand_name = brand_name
        self.kilometers = kilometers
        self.liters = liters

    def calculate_mpg(self):
        miles_driven = self.kilometers / 1.60934
        gallons_fueled =self.liters / 4.54609
        mpg = round(miles_driven / gallons_fueled, 2)
        return mpg

    def calculate_rate_of_gas(self, price):
        rate_of_gas = round(price / self.calculate_mpg(), 2)
        return rate_of_gas
        
new_car = Car("BMW I8 Roadster", 40, 1.5)
print(new_car.calculate_mpg())
print(new_car.calculate_rate_of_gas(250))