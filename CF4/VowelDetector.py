#use string maipulation
word = input("Please enter word: ")
vowels = "a, e, i, o, u"
#call out len() and .lower 
count = len(set(word.lower()) & set(vowels))
if count == 0:
  print("There are no vowels in the string.")
elif count == 1:
  print("There is only one different vowel in the string.")
else:
  print(f"There are {count} different vowels in the string.")