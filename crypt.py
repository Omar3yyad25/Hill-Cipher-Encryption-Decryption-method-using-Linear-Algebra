import numpy as np
import string
import random


def getMessage():
    message = input ('')

def encrypt(m :string):
    dimension =3
    key = np.matrix([[-1,2,0],[2,-4,-1],[0,1,1]])# Your key
    Originalmessage = m # Your message

    # Generate the alphabet
    alphabet = string.ascii_uppercase

    # Encrypted message
    encryptedMessage = ""

    # Group message in vectors and generate crypted message
    for index, i in enumerate(Originalmessage):
        values = []
        # Make bloc of N values
        if index % dimension == 0:
            for j in range(0, dimension):
                if(index + j < len(Originalmessage)):
                    values.append([alphabet.index(Originalmessage[index + j])])
                else:
                    values.append([random.randint(0,25)])
            # Generate vectors and work with them
            vector = np.matrix(values)
            vector = key * vector
            vector %= 26
            for j in range(0, dimension):
                encryptedMessage += alphabet[vector.item(j)]

    # Show the result
    return (encryptedMessage)
