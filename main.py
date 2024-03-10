#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
# Password=[]
# for n in range(1,nr_letters):
#   random_letter=random.choice(letters)
#   Password.append(random_letter)
# for n in range(1,nr_symbols):
#   random_symbol=random.choice(symbols)
#   Password.append(random_symbol)
# for n in range(1,nr_numbers):
#   random_number=random.choice(numbers)
#   Password.append(random_number)
# print("Your password is:",end=" ")
# for n in Password:
#   print(n,end="")

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

Possible_letter=[letters,numbers,symbols]
Password=[]
total_letter=nr_letters+nr_numbers+nr_symbols
for n in range(1,total_letter):
  random_choice=random.choice(Possible_letter)
  if random_choice==letters:
    random_letter=random.choice(letters)
    Password.append(random_letter)
  elif random_choice==numbers:
    random_number=random.choice(numbers)
    Password.append(random_number)
  else:
    random_symbol=random.choice(symbols)
    Password.append(random_symbol)

print("Your password is:",end=" ")
for n in Password:
  print(n,end="")

