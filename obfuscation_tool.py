import base64
import hashlib
import random
import time

text = input("Input text you want to obfuscate: ")
textsum = text.encode()

def obfuscation_service():
    base64_text = base64.b64encode(textsum)
    base32_text = base64.b32encode(textsum)
    base16_text = base64.b16encode(textsum)
    print("Text: ", text)
    print("Base64 text: ", base64_text)
    print("Base32 text: ", base32_text)
    print("Base16 text: ", base16_text)
    print("Writing obfuscation data + hashes into a txt file...")
    md5sumT = hashlib.md5(textsum).hexdigest()
    md5sum64 = hashlib.md5(base64_text).hexdigest()
    md5sum32 = hashlib.md5(base32_text).hexdigest()
    md5sum16 = hashlib.md5(base16_text).hexdigest()
    sha256sumT = hashlib.sha256(textsum).hexdigest()
    sha256sum64 = hashlib.sha256(base64_text).hexdigest()
    sha256sum32 = hashlib.sha256(base32_text).hexdigest()
    sha256sum16 = hashlib.sha256(base16_text).hexdigest()
    with open(f'obfuscation_log_{random.randint(1000, 9999)}.txt', 'w') as file:
        file.write("Text: " + text + "\n")
        file.write("Base64: " + base64_text.decode() + "\n")
        file.write("Base32: " + base32_text.decode() + "\n")
        file.write("Base16: " + base16_text.decode() + "\n")
        file.write("\n")
        file.write("MD5 hash text: " + md5sumT + "\n")
        file.write("MD5 hash base64: " + md5sum64 + "\n")
        file.write("MD5 hash base32: " + md5sum32 + "\n")
        file.write("MD5 hash base16: " + md5sum16 + "\n")
        file.write("SHA256 hash text: " + sha256sumT + "\n")
        file.write("SHA256 hash base64: " + sha256sum64 + "\n")
        file.write("SHA256 hash base32: " + sha256sum32 + "\n")
        file.write("SHA256 hash base16: " + sha256sum16 + "\n")



obfuscation_service()
time.sleep(4)