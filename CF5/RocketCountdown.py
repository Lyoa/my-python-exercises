# def countdown(n):
#   while n >= 0:
#     print(n)
#     n -= 1
#   print("Blast off!")

# countdown(5)

n = int(input("Countdown starts in: "))

for n in range(n-1, -1, -1):
  print(n + 1)

print("Blast off!")