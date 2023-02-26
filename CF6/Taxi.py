# def taxi(distance):
#   base_fare = 4.00
#   fare_per_km = 0.50
#   distancekm = distance / 1000
  
#   fare = base_fare + (distancekm * fare_per_km)
  
#   return "{:.2f}".format(fare)

def taxi(distance):
    baseFare = 4.00
    excessFare_140m = 1.00
    excessDistance = distance - 140
    if excessDistance > 0:
      excessFare = excessDistance / 140 * excessFare_140m
    else:
      excessFare = 0
      
    totalFare = baseFare + excessFare
    
    return "{:.2f}".format(totalFare)