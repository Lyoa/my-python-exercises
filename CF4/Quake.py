magn = float(input("Magnitude: "))

if magn < 2.0:
    print("Micro")
elif magn >= 2.0 and magn < 3.0:
    print("Very Minor")
elif magn >= 3.0 and magn < 4.0:
    print("Minor")
elif magn >= 4.0 and magn < 5.0:
    print("Light")
elif magn >= 5.0 and magn < 6.0:
    print("Moderate")
elif magn >= 6.0 and magn < 7.0:
    print("Strong")
elif magn >= 7.0 and magn < 8.0:
    print("Major")
elif magn >= 8.0 and magn < 10.0:
    print("Great")
elif magn >= 10.0:
    print("Meteoric")
else:
    pass
