import time

#hash comparison function
def comparison_service():

    #user input to choose what hashes to compare
    hash1 = input("Input the first hash: ")
    hash2 = input("Input the second hash: ")
    #print out chosen hashes
    print("First hash: ", hash1)
    print("Second hash: ", hash2)
    
    if hash1 == hash2:
        print("Hashes are the same.") #if hashes are the same
    else:
        print("Hashes are not the same.") #if hashes are not the same
    
comparison_service()
time.sleep(8)
