CurrentTime = 14
AlarmOff = 535
HoursInADay = 24

No_of_days = (AlarmOff / HoursInADay)
RemainingHours = (AlarmOff % HoursInADay)

print(f'{CurrentTime + RemainingHours:.2f}')