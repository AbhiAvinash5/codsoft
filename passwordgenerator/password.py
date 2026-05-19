import random
import string

print("PASSWORD GENERATOR")

while True:

    try:

        length = int(input("\nEnter password length: "))

        all_characters = string.ascii_letters + string.digits + string.punctuation

        password = ""

        for i in range(length):

            random_character = random.choice(all_characters)

            password = password + random_character

        print("\nGenerated Password:", password)

    except:

        print("\nPlease enter a valid number")

    choice = input("\nGenerate again? (yes/no): ")

    if choice.lower() != "yes":

        print("\nProgram Ended")

        break