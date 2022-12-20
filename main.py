from encrypt import AES256
from save import Saver
import os

masterPasswordCheck = b'a1DOnVGLGvq08ZI2MigPQyLVHvFhEM65IXARiCfov+Y='


saver = Saver("passwords.txt")
passwords = saver.read()
loggedIn = False

while True:
    if not loggedIn:
        print("Master Password: ", end="")
        masterPassword = input()

        encrypter = AES256(masterPassword)

        if encrypter.encrypt("textToMatch") != masterPasswordCheck:
            print("Password Incorrect")
            input()
            continue
        else:
            loggedIn = True

    os.system("clear")

    print("1. Find Password")
    print("2. Add Password")
    print("3. Delete Password")

    print("\nChoice: ", end="")
    choice = int(input())

    if choice < 1 or choice > 3:
        print("Choice needs to be a number from 1-3")
        input()
        continue

    print("Application Name: ", end="")
    app = input()

    if choice == 1:
        for entry in passwords:
            if app in encrypter.decrypt(entry[0]):
                print("\n-----------------------------------------")
                print(f"Application: {encrypter.decrypt(entry[0])}")
                print(f"Password: {encrypter.decrypt(entry[1])}")
        input()

    elif choice == 2:
        print("Password: ", end="")
        password = input()

        passwords.append([encrypter.encrypt(app).decode(), encrypter.encrypt(password).decode()])
        saver.save(passwords)

    elif choice == 3:
        for entry in passwords:
            if app == encrypter.decrypt(entry[0]):
                print(f"Are you sure want to delete '{app}' [y/n]: ", end="")
                comfirm = input()

                if comfirm == "y":
                    del passwords[passwords.index(entry)]
                    saver.save(passwords)
                
                break
