import secrets
import string

#provide password label
#generate a password based off the requirements
#store it in a txt file

def password():
    chars = string.ascii_letters
    altchars = string.digits + string.punctuation
    allchars = chars + altchars

    label = input("password label: ").strip()

    while not label:
        label = input("Label cannot be blank. Declare label: ").strip()
        while not label:
            label = input("Label cannot be blank. Declare label: ").strip()

    while True:
        user_length = input("Password length (default=14, max=25): ").strip()
    
        if user_length == "":
            length = 14
            break
        
        if user_length.isdigit():
            length = int(user_length)
        
            if 8 <= length <= 25:
                break
            else:
                print("Error: Length must be between 8 and 25.")
        else:
            print("Error: Please enter a valid number.")


    spchars = input("Include special characters/digits?(y/press enter to skip): ").strip()

    password = ""

    if spchars.lower() == "y":
        for i in range(length):
            single_char = secrets.choice(allchars)
            password += single_char

    else:
        for i in range(length):
            single_char = secrets.choice(chars)
            password += single_char

    print(label, ": ", password)

if __name__ == "__main__":
    password()

