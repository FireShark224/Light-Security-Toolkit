import cryptography #import the cryptography library
from cryptography import fernet
import time
import random
import hashlib


key = fernet.Fernet.generate_key() #generate a key
tool_encrypt = fernet.Fernet(key) #variable that uses the key 

def encryption_service():
    text = input("text you want to encrypt:")
    encrypted_text = tool_encrypt.encrypt(text.encode()) #encryption process
    print("your text:", text)
    print("encrypted text:", encrypted_text)
    print("encryption key:", key)
    print("writing encryption data + hashes into a txt file...")
    md5sumT = hashlib.md5(text.encode()).hexdigest()
    md5sumK = hashlib.md5(key).hexdigest()
    md5sumE = hashlib.md5(encrypted_text).hexdigest()
    sha256sumT = hashlib.sha256(text.encode()).hexdigest()
    sha256sumK = hashlib.sha256(key).hexdigest()
    sha256sumE = hashlib.sha256(encrypted_text).hexdigest()
    with open(f'encryption_log_{random.randint(1000, 9999)}.txt', 'w') as file:
        file.write("encrypted text: " + encrypted_text.decode() + "\n") #decode from bytes to readable string
        file.write("key: " + key.decode() + "\n")
        file.write("user input: " + text + "\n")
        file.write("\n")
        file.write("MD5 hash text: " + md5sumT + "\n")
        file.write("MD5 hash key: " + md5sumK + "\n")
        file.write("MD5 hash encrypted: " + md5sumE + "\n")
        file.write("SHA256 hash text: " + sha256sumT + "\n")
        file.write("SHA256 hash key: " + sha256sumK + "\n")
        file.write("SHA256 hash encrypted: " + sha256sumE + "\n")

        
encryption_service()
time.sleep(4) # code made by FireShark224