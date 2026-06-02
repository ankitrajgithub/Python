#Encryption Program
import random
import string

chars=" "+string.punctuation+string.digits+string.ascii_letters
chars=list(chars)

key=chars.copy()
random.shuffle(key)

def encrypt():
    plain_text=input("Enter a message to encrypt : ")
    cipher_text=""
    for letter in plain_text:
        index=chars.index(letter)
        cipher_text+=key[index]
    print(f"Encrypted Message : {cipher_text}")

def decrypt():
    cipher_text=input("Enter a message to decrypt : ")
    plain_text=""
    for letter in cipher_text:
        index=key.index(letter)
        plain_text+=chars[index]
    print(f"Decrypted Message : {plain_text}")

if __name__=="__main__":
    encrypt()
    decrypt()