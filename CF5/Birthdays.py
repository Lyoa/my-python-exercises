# # n = int(input("Shem's age: "))
# # x = float(input("Price of washing machine: "))
# # p = float(input("Price of toys sold: "))
# # #look for another opt
# # total = 0

# # for i in range(2,n + 1, 2):
# #   total += 10 + (i - 2) * 10
# # total += (n // 2) * p

# # #recompute!
# # #failed in quiz - something in formula/computation
# # if total - x >= 0:
# #   print("Yes! you still have {:.2f} left".format(total-x))
# # else:
# #   print("No! you still need {:.2f}".format(x-total))

# n = int(input("Shem's age: "))
# x = float(input("Price of washing machine: "))
# p = float(input("Price of toys sold: "))
# #opt 2
# total = 0

# for i in range(2,n + 1, 2):
#   total += 10 * (i // 2)
# #- stolen by her brother
# total -= (n // 2)
# #acquired from selling her toyd
# total += p *((n * 1) // 2)
# #final comp == if money is enough to buy WM
# if total >= x:
#   print("Yes! you still have {:.2f} left".format(total - x))
# else:
#   print("No! you still need {:.2f}".format(x - total))

n = int(input())
x = float(input())
p = float(input())

total = 0
for i in range(1, n+1):
    if i % 2 == 0:
        total += 10 * (i//2) - 1
    else:
        total += p

if total >= x:
    # print(f"Yes! you still have {round(total-x, 2)} left")
    print("Yes! you still have {:.2f} left".format(total - x))
else:
    # print(f"No! you still need {round(x-total, 2)}")
    print("No! you still need {:.2f}".format(x - total))