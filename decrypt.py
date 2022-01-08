import numpy as np
from sympy import Matrix
import string

def decyrpt(x: string):
    dim= 3  #The dimension of the square matrix
    keyMatrix = np.matrix([[-1, 2, 0], [2, -4, -1], [0, 1, 1]]) # The matrix key
    Encryptedmessage = x   #the word which got from the argument

    letters = string.ascii_letters #corresponding each letter to ascii table

    decryptedMessage = ""  #initialize the decrypted message

    keyMatrix = Matrix(keyMatrix)
    keyMatrix = keyMatrix.inv_mod(26)    # These functions to reverse the encrypt process
    keyMatrix = keyMatrix.tolist()

                    # put the corresponding value in form of vectors to get the original message
    for index, i in enumerate(Encryptedmessage):
        values = []
        if index % dim == 0:
            for j in range(0, dim):
                values.append([letters.index(Encryptedmessage[index + j])])
            vector = np.matrix(values)
            vector = keyMatrix * vector
            vector %= 26
            for j in range(0, dimension):
                decryptedMessage += letters[vector.item(j)]
    return (decryptedMessage) #return the message
