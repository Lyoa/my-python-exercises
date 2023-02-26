# # Ask for the number of enrollees
# n = int(input("How many enrollees? "))

# # Initialize counters
# males = 0
# females = 0

# Loop to get input
# for i in range(n):
#     gender = input("Enter gender (M/F): ")

#     # Count males and females
#     if gender.lower() == 'm':
#         males += 1
#     elif gender.lower() == 'f':
#         females += 1

# # Print results
# print(f"Males: {males}")
# print(f"Females: {females}")

# # Calculate ratio (in lowest terms)
# if males > females:
#     ratio = males // females
# else:
#     ratio = females // males

# print(f"Male-to-Female Ratio: {ratio}")


# n = int(input("How many enrollees? "))

# males = 0
# females = 0

# for i in range(n):
#     gender = input("Enter gender (m/f): ")

#     if gender.lower() == 'm':
#         males += 1
#     elif gender.lower() == 'f':
#         females += 1

# print(f"Males: {males}")
# print(f"Females: {females}")

# if males == 0:
#    print("All females")
# elif females == 0:
#     print("All males")
# else:
#     ratio = f"{males}:{females}"
#     print(ratio)

# n = int(input("How many enrollees? "))

# males = 0
# females = 0

# for i in range(n):
#     gender = input("Enter gender (m/f): ")

#     if gender.lower() == 'm':
#         males += 1
#     elif gender.lower() == 'f':
#         females += 1

# print(f"Males: {males}")
# print(f"Females: {females}")

# if males == 0:
#    print("All females")
# elif females == 0:
#     print("All males")
# else:
#     ratio = f"{males//females}:{females//males}"
#     print(ratio)

# n = int(input("How many enrollees? "))

# males = 0
# females = 0

# for i in range(n):
#     gender = input("Enter gender (m/f): ")

#     if gender.lower() == 'm':
#         males += 1
#     elif gender.lower() == 'f':
#         females += 1

# print(f"Males: {males}\nFemales: {females}")

# for n in range(n):
#         if males == 0:
#             print("All females")
#         elif females == 0:
#             print("All males")
# else:
#     ratio = f"{males//females}:{females//males}"

# print(ratio)

n = int(input("How many enrollees? "))

males = 0
females = 0

for i in range(n):
    gender = input("Enter gender (m/f): ")

    if gender.lower() == 'm':
        males += 1
    elif gender.lower() == 'f':
        females += 1

print(f"Males: {males}\nFemales: {females}")

if males == 0:
    print("All females")
elif females == 0:
    print("All males")
else:
    # GCD
    gcd = males
    while females % gcd != 0:
        gcd -= 1

    ratio = f"{males//gcd}:{females//gcd}"
    print(ratio)
