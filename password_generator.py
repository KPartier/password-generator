import secrets

# Read characters from file (characters.txt) to use in password generation

def get_character_list():

    full_character_list = []
    
    with open('characters.txt', 'r') as character_file:
        characters = character_file.read()
        characters_list = characters.split()
        
    full_character_list = characters_list
    return full_character_list


# Generate password function using secrets library

# secrets.choice produces a cryptographically secure random number, which then applies to  the get_character_list function - the result being a random character chosen from the list. This repeats until the user-defined password length is reached.

def generate_password(password_length):

        password = ''.join(secrets.choice(get_character_list()) for i in range(password_length))
        print("")
        print(password)
        

# Options for password length and amount

pw_length = input("Enter the desired length of passwords (number of characters or words): ")

pw_amount = input("Enter the number of passwords to generate: ")
print("Number: " + pw_amount)

# Convert entered password lengths and amounts to numbers

pl = int(pw_length)
pa = int(pw_amount)

# Generate passwords

p = 0

while p < pa:
    generate_password(pl)
    p = p + 1

print("")
print("##########################################")
print("Generation complete.")
print("##########################################")
print("")


    
    
    
    

