import random 
chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890-+=!@#$%^&*"
length_of_pass = int(input("Enter the length of the password: "))
def pass_generator(num):
    password = ''
    for i in range(num):
        password += random.choice(chars)
    return password
print(pass_generator(length_of_pass))
