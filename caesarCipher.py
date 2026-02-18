word = input("what is your word: ")


def encryptCaesar(word):
    result = ""
    for letter in word:
        encrypted = ord(letter) + 3

        if letter.isupper() and encrypted > ord('Z'):
            encrypted -= 26
        elif letter.islower() and encrypted > ord('z'):
            encrypted -= 26

        result += chr(encrypted)
    return result

def decryptCaesar(word):
    result = ""
    for letter in word:
        decrypt = ord(letter) - 3

        if letter.isupper() and decrypt < ord('A'):
            decrypt += 26
        elif letter.islower() and decrypt < ord('a'):
            decrypt += 26

        result += chr(decrypt)
    return result

encrypted = encryptCaesar(word)
print("encrypted: " + encrypted)
print("decrypted: " + decryptCaesar(encrypted))    