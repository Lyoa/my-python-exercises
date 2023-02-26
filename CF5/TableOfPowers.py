# # Python Program to Print Powers Table  
# M = int(input())
# N = int(input())
# P = int(input())
  
# for x in range(M, N + 1): 

#     print() 
      
#     # Prints powers of particular base 
#     for y in range(2, P + 1): 
#         print("\t", x ** y, end = "") 
    
#     print()

#take input
# M = int(input())
# N = int(input())
# P = int(input())

# #print the table
# for i in range(M, N+1):
#     for j in range(2, P+1):
#         print(i**j, end = ',')
#     print()


# M = int(input())
# N = int(input())
# P = int(input())
# # Iterate through the range of bases from M to N
# for base in range(M, N+1):
#   # Initialize an empty list to store the powers of the current base
#   powers = []
  
#   # Iterate through the range of powers from 2 to P
#   for power in range(2, P+1):
#     # Compute the power and append it to the list
#     powers.append(base**power)
  
#   # Convert the list of powers to a string and join the elements with commas
#   powers_str = ",".join(str(power) for power in powers)
  
#   # Print the powers for the current base
#   print(powers_str)

#  = int(input())
# N = int(input())
# P = int(input()) 

# def print_power_table(m, n, p):

#     for base in range(m, n+1):
#         row = ""
#     for power in range(2, p+1):
#       row += str(base**power) + ", "
#     print(row[:-2])  # remove the last ", " from the row

# print_power_table(7, 14, 5)

def main():

  m = int(input())
  n = int(input())
  p = int(input()) 

  for base in range(m, n+1):
    row = []
    for power in range(2, p+1):
      row.append(str(base ** power))
    print(', '.join(row))
 
  
