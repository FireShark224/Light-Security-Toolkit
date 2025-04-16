import time

def comparison_service():
    hash1 = input("Input the first hash: ")
    hash2 = input("Input the second hash: ")
    print("First hash: ", hash1)
    print("Second hash: ", hash2)
    if hash1 == hash2:
        print("Hashes are the same.")
    else:
        print("Hashes are not the same.")
    
comparison_service()
time.sleep(8)