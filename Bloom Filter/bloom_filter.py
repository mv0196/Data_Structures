import pyhash
#Step 1: make bit_vector of required length
bit_vector=[0]*20
#Step 2: get the non-cryptographic fumctions
fnv=pyhash.fnv1_32()
murmur=pyhash.murmur3_32()
#Step 3: calculate the value calculated by the functions
fnv_pika=fnv("Pikachu")%20
murmur_pika=murmur("Pikachu")%20
fnv_char=fnv("charmander")%20
murmur_char=murmur("Vharmander")%20
#Step 4: Turn On the bits calculated by the function in the bit_vector
bit_vector[fnv_pika]=bit_vector[murmur_pika]=1
bit_vector[fnv_char]=bit_vector[murmur_char]=1
#Let us assume we found a new entry and we want to check wether this entry alredy exists or note
#Step 5: For lookups find the value calculated by the functions for that entry and look the value at that location i the bit_vector
#if the value at both the calculated locations are ON the the entry may n\be already present(There may be a acse of False Positives)
#lets say we found a new entry "Bulbasaur" and we want to find that wether it is already present or note
def lookup(s):
    fnv_bulb=fnv(s)%20
    murmur_bulb=murmur(s)%20
    if bit_vector[fnv_bulb] and bit_vector[murmur_bulb]:
        print(s," might be present")
    else:
        print(s," is not present")
lookup("Bulbasaur")
