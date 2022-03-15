import random

characters: str = "!@#$%-_1234567890qwertyuiopasdfghjklzxcvbnm"
password: str = None

length: int = None

print("What would you like the length of the password to be? (Min 3 characters, Max 100)")
length = int(input())

def generatePassword():
    if not length in range(3, 100):
        return
    
    password = ""

    for index in range(length):
        password += characters[random.randint(0, len(characters) - 1)]
            
    print(password)

generatePassword()
