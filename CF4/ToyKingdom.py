import math

targetDonation = float(input("Target Donation: "))
NPuzzle = int(input("Number of Puzzles: "))
NTalkingDoll = int(input("Number of Talking Dolls: "))
NTeddyBear = int(input("Number of Teddy Bears: "))
NPokemonPlushie = int(input("Number of Pokemon Plushies: "))
NBigToyTruck = int(input("Number of Big Toy Trucks: "))

totalCount= NPuzzle + NTalkingDoll + NTeddyBear + NPokemonPlushie +NBigToyTruck

CPuzzle = NPuzzle * 14
CTalkingDoll = NTalkingDoll * 3
CTeddyBear = NTeddyBear * 20.2
CPokemonPlushie = NPokemonPlushie * 8.20
CBigToyTruck = NBigToyTruck * 10.65

totalCost = CPuzzle + CTalkingDoll + CTeddyBear + CPokemonPlushie + CBigToyTruck

if totalCount >= 50:
    totalCost = totalCost * 0.75

rentalCost = totalCost * 0.1
remainingCost = totalCost - rentalCost

if remainingCost >= targetDonation:
    print(f"Yes! {remainingCost - targetDonation:.2f} dollars left. ")
else:
    print(f"Not enough money! {targetDonation - remainingCost:.2f} dollars needed.")
