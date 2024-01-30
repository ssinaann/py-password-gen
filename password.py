import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

ltrs=''
nums=''
symbs=''
for i in range(0, nr_letters):
  random_index1 = random.randint(0,len(letters)-1)
  ltrs=ltrs+letters[random_index1]
for k in range(0,nr_symbols):
  random_index2 = random.randint(0,len(symbols)-1)
  symbs=symbs+symbols[random_index2]
for j in range(0,nr_numbers):
  random_index3 = random.randint(0,len(numbers)-1)
  nums=nums+numbers[random_index3]
   
password = ltrs+nums+symbs
print(f'Your generated password is: {password}')
