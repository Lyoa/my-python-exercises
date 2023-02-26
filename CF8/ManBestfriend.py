# class Dog:
#     def __init__(self, name, breed):
#         self.name = name
#         self.breed = breed

#     def bark(self):
#         print(f"{self.name} is barking")

#     def run(self):
#         print(f"{self.name} is running.")

#     def eat(self, food):
#         print(f"The dog is eating {food}.")

#     def play(self, toy):
#         if toy[0].lower() in ['a', 'e', 'i', 'o', 'u']:
#             print(f"Playing with an {toy}")
#         else:
#             print(f"Playing with a {toy}")

# name = input()
# breed = input()
# dog = Dog(name, breed)
# dog.bark()

# class Dog:
#     def __init__(self, name, breed):
#         self.name = name
#         self.breed = breed
        
#         name = input()
#         breed = input()
        
#     def bark(self):
#         print(f"{self.name} is barking", self.dog.bark)

#     def run(self):
#         print(f"{self.name} is running", self.dog.run)

#     def eat(self, food):
#         print(f"The dog is eating {food}.")

#     def play(self, toy):
#         if toy[0].lower() in ['a', 'e', 'i', 'o', 'u']:
#             print(f"Playing with an {toy}")
#         else:
#             print(f"Playing with a {toy}")

class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print(f"{self.name} is barking")
        return self.name + ' is barking'

    def run(self):
        print(f"{self.name} is running")
        return self.name + ' is running'

    def eat(self, food):
        print(f"{self.name} is eating {food}.")
        return self.name + f' is eating {food}'

    def play(self, toy):
      if toy[0].lower() in ['a', 'e', 'i', 'o', 'u']:
        print(f"{self.name} is playing with an {toy}")
        return self.name + f" is playing with an {toy}"
      else: 
        return f"{self.name} is playing with a {toy}"
        


        




