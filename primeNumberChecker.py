#PRIME NUMBER CHECKER
#Prime numbers are numbers that can only be cleanly divided by themselves and 1.
#You need to write a function that checks whether if the number passed into it is a prime number or not.
#Example outputs: It's a prime number. It's not a prime number.

#Write your code below this line 👇
def prime_checker(number):
  #if (number % number == 0 and ):
   factors = 0
   for iteration in range(1,number+1):
     if number % iteration == 0:
       factors += 1
       
   if factors == 2:
      print("It's a prime number")
   else:
      print("It's not a prime number")


#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)

