import os

def insecure_function():
    # Insecure: Using os.system() without sanitizing input
    user_input = input("Enter command: ")
    os.system(user_input)

if __name__ == "__main__":
    insecure_function()
