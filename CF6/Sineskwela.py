# def commoncharacters( w1, w2 ):
#     common = ""
#     for letter in w1:
#         if (letter in w2) and (letter not in common):
#             common += letter
#     num = len( common )        
#     return check(num)
    
# def check(num):
#     if num <= 0:
#         return "The words share no characters"
#     elif num == 1:
#         return "The words have one character in common"
#     else:
#         return "The words have {} characters in common".format(num)

def commoncharacters(w1, w2):
   set1 = set(w1)
   set2 = set(w2)
   common_char = set1.intersection(set2)
   num_common_chars = len(common_char)
   
   if num_common_chars == 0:
      return 'The words share no characters'
   elif num_common_chars == 1:
      return 'The words have one character in common'
   else:
      return f'The words have {num_common_chars} characters'
    
print(commoncharacters('dead', 'deed'))

