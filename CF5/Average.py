val = []
avg = 0 

while True:
    num = float(input("Enter a number: "))
    if num > 0:
        val.append(num)
    else:
        avg = sum(val)/len(val)
        print(int(avg))
        break