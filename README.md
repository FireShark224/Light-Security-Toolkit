# Light-Security-Toolkit
Want some easy and light security tasks done? (light security in a sense that you only need fast, lightweight tools and not enterprise level tools)
Here are some basic tools written in Python made for light security tasks, like encrypting passwords, obfuscating text, hashing data etc.
The 5 tools are:
1 - encryption_tool: You just have to input text, it will generate a key, and encrypt the text using the key, and generate MD5 and SHA256 hashes of text, key, and encrypted text it will write all of this data into a txt file under a name "encryption_log_xxxx" the 'xxxx' will be a random value from 1000 to 9999.
2 - decryption_tool: You just input the key and then encrypted text and this tool will decrypt the text, and write the key used, encrypted value given and the result of decription into a txt file under a name "decryption_log_xxxx" the 'xxxx' will be a random value from 1000 to 9999.
3 - hash_comparison_tool: You just input 2 hash strings, and the program will print out whether both hashes match.
4 - obfuscation_tool: You just have to input text, it will automatically obfuscate it and write the original text, and obfuscations made in Base64,Base32,Base16 along with MD5 and SHA256 hashes of text, base64, base32, base16 strings, it will write all of this data into a txt file with a name "obfuscation_log_xxxx" the 'xxxx' will be a random value from 1000 to 9999.
5 - de-obfuscation_tool: You just have to pick whether you want to de-obfuscate in Base64, Base32 or Base16, then input the obfuscated string in the Base you chose, it will de-obfuscate the value and write it and the original input into a txt file under a name "de-obfuscation_log_xxxx" the 'xxxx' will be a random number from 1000 to 9999.

Thanks for using! 
Made by FireShark224

Required libraries:
base64, hashlib, time, random, cryptography, cryptography-fernet.
