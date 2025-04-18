import base64
import time
import random

print("Which base do you want to de-obfuscate?")
print("Base64 = 1, Base32 = 2, Base16 = 3")
option = input("Choose: ") #choose the base to de-obfuscate

#function that handles de-obfuscation process
def deobfuscation_service():

    #handle all possible options
    if option == "1": #option 1 handle base64
        base64in = input("Input base64 string: ")
        base64ou = base64.b64decode(base64in).decode() #decode the base64 string
        print("Input: ", base64in)
        print("Output: ", base64ou)
        print("Writing de-obfuscation data into a txt file...")
        with open(f'de-obfuscation_log_{random.randint(1000, 9999)}.txt', 'w') as file: #write data into a file
           file.write("Base64: " + base64in + "\n")
           file.write("Base64 de-obfuscated: " + base64ou + "\n")
    elif option == "2": #option 2 handle base32
     base32in = input("Input base32 string: ")
     base32ou = base64.b32decode(base32in).decode() #decode the base32 string
     print("Input: ", base32in)
     print("Output: ", base32ou)
     print("Writing de-obfuscation data into a txt file...")
     with open(f'de-obfuscation_log_{random.randint(1000, 9999)}.txt', 'w') as file: #write data into a file
           file.write("Base32: " + base32in + "\n")
           file.write("Base32 de-obfuscated: " + base32ou + "\n")
    elif option == "3": #option 3 handle base16
       base16in = input("Input base16 string: ")
       base16ou = base64.b16decode(base16in).decode() #decode the base16 string
       print("Input: ", base16in)
       print("Output: ", base16ou)
       print("Writing de-obfuscation data into a txt file...")
       with open(f'de-obfuscation_log_{random.randint(1000, 9999)}.txt', 'w') as file: #write data into a file
           file.write("Base16: " + base16in + "\n")
           file.write("Base16 de-obfuscated: " + base16ou + "\n")



deobfuscation_service()
time.sleep(4)
