#factorial = n! / sample: 5! = 5*4*3*2*1 = 120
#use loops not library

x = int(input("Factorial of: "))
factorial = 1

for n in range(1, x+1):
    factorial *= n

print(factorial)