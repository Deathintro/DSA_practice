#Random password generator
import random

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!','@','#','$','%','^','&','*',')','(']

print("Welcome to pypassword generator")
num_of_letters = int(input("How many letters would you like in your password?\n"))
num_of_numbers = int(input("How many numbers would you like?\n"))
num_of_symbols = int(input("How many symbols would you like?\n"))

result = []

for i in range(num_of_letters):
    result += random.choice(letters)
    
for i in range(num_of_numbers):
    result += random.choice(numbers)

for i in range(num_of_symbols):
    result += random.choice(symbols)
    
random.shuffle(result)
fin_res = ''
for i in result:
    fin_res += i

print(f"Your password is: {fin_res}")