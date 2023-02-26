grade = float(input("Enter the grade: "))

if grade % 0.5 != 0:
  grade = round(grade * 2) / 2
  print("Grades should be rounded to the nearest half point.")
else:
  if grade < 0 or grade > 10:
    print("Grades should be between zero and 10.")
  else:
    if grade >= 8.5:
      print("Grade A")
    elif grade >= 7.5:
      print("Grade B")
    elif grade >= 6.5:
      print("Grade C")
    elif grade >= 5.5:
      print("Grade D")
    else:
      print("Grade F")