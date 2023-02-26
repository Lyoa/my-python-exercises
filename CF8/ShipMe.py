# import math

# class Package:
#     def __init__(self, weight, distance):
#         self.weight = weight
#         self.distance = distance
#         self.shipping_fee = 0
#         self.tax = 0
#         self.total_fee = 0

#     def calculate_shipping_fee(self):
#         if self.distance <= 100:
#             self.shipping_fee = 45
#         else:
#             self.shipping_fee = 50 + (self.distance - 100) * 1.5
#         return self.shipping_fee

#     def calculate_tax(self):
#         self.tax = self.weight * 0.25
#         return self.tax
    
#     def calculate_total_fee(self):
#         self.total_fee = round(self.shipping_fee + self.tax, 2)
#         return self.total_fee

# class Package:
#     def __init__(self, weight, distance):

#     @property
#     def weight(self):

#     @weight.setter
#     def weight(self, value):

#     @property
#     def distance(self):

#     @distance.setter
#     def distance(self, value):

#     @property
#     def shipping_fee(self):

#     @shipping_fee.setter:
#     def shipping_fee(self, value):

#     @property
#     def added_shipping_tax(self):

#     @added_shipping_tax.setter:
#     def added_shipping_tax(self, value):

#     @property
#     def total_shipping_fee(self):

class Package:

    def __init__(self, weight, distance):
        self._weight = weight
        self._distance = distance

    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, value):
        self._weight = value
        self.added_shipping_tax = self._weight

    @property
    def distance(self):
        return self._distance

    @distance.setter
    def distance(self, value):
        self._distance = value
        self.shipping_fee = self._distance

    @property
    def shipping_fee(self):
        return self._shipping_fee

    @shipping_fee.setter
    def shipping_fee(self, value):
        if value < 2:
            self._shipping_fee = 0
        elif value < 100:
            self._shipping_fee = 45
        else:
            self._shipping_fee = ((value // 100) * 50) + ((value % 100) * 1.50)

    @property
    def added_shipping_tax(self):
        return self._added_shipping_tax

    @added_shipping_tax.setter
    def added_shipping_tax(self, value):
        if value >= 1:
            self._added_shipping_tax = value * 0.25
        else:
            self._added_shipping_tax = 0

    @property
    def total_shipping_fee(self):
        self._total_shipping_fee = round((self._shipping_fee + self._added_shipping_tax),2)
        return self._total_shipping_fee
