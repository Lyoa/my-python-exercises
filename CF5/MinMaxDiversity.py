highest = 0
lowest = 0
divisible_by_3 = 0

for i in range(10):
    num = int(input("Enter a number: "))

    #highest
    if num > highest:
        highest = num

    #lowest
    if lowest == 0 or num < lowest:
        lowest = num

    #numbers divisible by 3
    if num % 3 == 0:
        divisible_by_3 += 1

print("Highest:", highest)
print("Lowest:", lowest)
print(divisible_by_3, "numbers divisible by 3")

