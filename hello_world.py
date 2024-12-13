# print("Hallo World!")

# # password test
# def connect_to_service():
#     password = "test123"
#     print("Connecting to service with password:", password)

# if __name__ == "__main__":
#     connect_to_service()

# insecure_script.py

import os

def insecure_function():
    # Insecure: Using os.system() without sanitizing input
    user_input = input("Enter command: ")
    os.system(user_input)

if __name__ == "__main__":
    insecure_function()
