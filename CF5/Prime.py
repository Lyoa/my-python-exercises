num = int(input())

# prime numbers are greater than 1
if num > 1:
   # check for factors
   for i in range(2,num):
       if (num % i) == 0:
           print("Not Prime")
           break
   else:
       print("Prime")
       
# if input number is less than or equal to 1, it is not prime
else:
# print(num,"Not Prime")
    print("Not Prime")