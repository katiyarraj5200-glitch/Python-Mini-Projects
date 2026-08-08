import random
import string

# Function to generate a strong WiFi password 

def generate_password(length = 16):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Generate and print password
print("Your WiFi Password : ", generate_password())
