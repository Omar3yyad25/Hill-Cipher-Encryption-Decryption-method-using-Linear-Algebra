import numpy as np
import string
import random


def getMessage():
    message = input ('')

def encrypt(m :string):
    dim =3 #The dimension of the square matrix
    keyMatrix = np.matrix([[-1,2,0],[2,-4,-1],[0,1,1]]) # The matrix key
    Originalmessage = m #the word which got from the argument

    alphabet = string.ascii_letters ##corresponding each letter to ascii table

    encryptedMessage ='' #initialize the encrypted message

          # put the corresponding value in form of vectors to get the encrypted message
    for index, i in enumerate(Originalmessage):
        values = []
        # Make bloc of N values
        if index % dim == 0:
            for j in range(0, dim):
                if(index + j < len(Originalmessage)):
                    values.append([alphabet.index(Originalmessage[index + j])])
                else:
                    values.append([random.randint(0,25)])
            vector = np.matrix(values)
            vector = keyMatrix * vector
            vector %= 26
            for j in range(0, dim):
                encryptedMessage += alphabet[vector.item(j)]

    return (encryptedMessage) #show the encrypt message
