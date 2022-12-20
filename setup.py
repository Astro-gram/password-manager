from encrypt import AES256

print("Enter your master password: ", end="")
masterPassword = input()

encrypter = AES256(masterPassword)

print(f"\nYour master password check is: {encrypter.encrypt('textToMatch')}")

print("Delete this file (setup.py) after you put the value into the variable 'masterPasswordCheck' in main.py")