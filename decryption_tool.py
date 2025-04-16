import cryptography 
from cryptography import fernet
import time
import random


key = input("Input the encryption key: ") #user input for the key
encrypted_text = input("Input the encrypted text: ") #user input for the encrypted text
keysum = key.encode() #turn the key string into bytes
tool_decrypt = fernet.Fernet(key) #variable that uses the key

def decryption_service():
    decrypted_text = fernet.Fernet(key).decrypt(encrypted_text) #decryption process
    print("your key: ", key)
    print("your encrypted text: ", encrypted_text)
    print("the decrypted result: ", decrypted_text)
    print("writing decrypted data into a txt file...")
    with open(f'decryption_log_{random.randint(1000, 9999)}.txt', 'w') as file:
        file.write("key: " + key + "\n" )
        file.write("encrypted text: " + encrypted_text + "\n")
        file.write("decrypted text: " + decrypted_text.decode() + "\n")


decryption_service()
time.sleep(4) # code made by FireShark224