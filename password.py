import random
import string

def generate_password(length, complexity):
    if complexity == 1:
        characters = string.ascii_lowercase
    elif complexity == 2:
        characters = string.ascii_letters
    elif complexity == 3:
        characters = string.ascii_letters + string.digits + string.punctuation
    else:
        return "Invalid complexity level!"

  
    password = ''.join(random.choice(characters) for _ in range(length))
    return password


length = int(input("Enter the length of the password: "))
print("Complexity Levels: 1 (Low), 2 (Medium), 3 (High)")
complexity = int(input("Enter the complexity of the password (1, 2, or 3): "))


generated_password = generate_password(length, complexity)
print(f"Generated Password: {generated_password}")