import random 
chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890-+=!@#$%^&*"
length_of_pass = int(input("num of letters:"))
def pass_generator(num):
    password = ''
    for i in range(num):
        password += random.choice(chars)
    return password
print(pass_generator(length_of_pass))
