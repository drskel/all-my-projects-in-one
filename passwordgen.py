import random

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()'
password = ''

def generate_password(length):
    global password
    password = ''.join(random.choice(chars) for _ in range(length))
    return password
if __name__ == "__main__":
    length = int(input("Enter the desired password length(MUST BE OVER 10): "))
    print("Generated Password:", generate_password(length))
    if length < 10:
        print("Warning: Password length is less than 10 characters, which may not be secure.")
    else:
        print("Your password is secure.")
    generate_password(length)