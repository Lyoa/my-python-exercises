# def capitalize(s):
#     capitalize = []
#     capitalize_sentences = []
#     words = []
#     # Capitalize the first char
#     capitalize.append(s[0].upper()) #index
    
#     for i in range(1, len(s)):
#         if s[i-1] != ' ' and s[i] == 'i':
#             capitalize.append('i')
#         elif s[i] in ['.', '!', '?']:
#             j = i + 1
#             while j < len(s) and s[j] == ' ':
#                 j += 1
#             if j < len(s):
#                 capitalize.append(s[j].upper())
#             else:
#                 capitalize.append(s[i])
#         else:
#             capitalize.append(s[i])

#         capitalize_sentences.append(" ".join(words))

#     capitalize_string = "".join(capitalize_sentences)
#     return ''.join(capitalize)

# print(capitalize("what time do i have to be there? what's the address? "))
# print(capitalize("What is your Name? "))
# print(capitalize("i will help you. you and i will finish it "))
# print(capitalize("hello, my name is Shay. I work as a software developer at a company "))


# def capitalize(str):
  
#     words = str.split()
    
#     words = [word.lower() for word in words]
    
#     words[0] = words.capitalize()

#     for i in range(0, len(words)):
#         if words [i-1][-1] in ".!?":
#             words[i] = words[1].capitalize()
#         elif words == 0 in ".!?":
#             words[1] = words[1].capitalize()

#         else:
#             sub = list(words[i])
#             for char in range (0, len(sub)):
#                 if sub[char] in ".!?" and char != len(sub) - 1:
#                     sub[char+1] = sub[char + 1].capitalize()
#                     words[1] = "".join(sub)

#     capital = " ".join(words)
#     capital = -capital.replace(" i ", " I ").replace(" i", " I").replace(" i ", " I ")
#     return capital

# print(capitalize("what time do i have to be there? what's the address? "))
# print(capitalize("What is your Name? "))
# print(capitalize("i will help you. you and i will finish it "))
# print(capitalize("hello, my name is Shay. I work as a software developer at a company "))
# print(capitalize("hi there, goodday! "))

# def capitalize(s):
   
#     words = s.split()
#     words[0] = words[0].capitalize()

#     for i in range(1, len(words)):
#         if words[i - 1][-1] in ".!?":
#             words[i] = words[i].capitalize()

#     s = ' '.join(words)
#     s = s.replace(" i ", " I ")
#     return s

# print(capitalize("what time do i have to be there? what's the address?"))
# print(capitalize("what is your name? "))
# print(capitalize("mike and i went to the mall"))

def capitalize(s):
    words = s.split()
    words[0] = words[0].title()

    for i in range(1, len(words)):
        if words[i - 1][-1] in ".!?":
            words[i] = words[i].title()

    s = ' '.join(words)
    s = s.replace(" i ", " I ")
    return s

print(capitalize('what is your name? '))
print(capitalize('Mike and i went to the mall '))
