import tkinter
from crypt import *
from decrypt import *
from tkinter import *


def clickEncrypt():
    result = Label ("The encrypted message is:" + encrypt(messageEntry.get()))
    result.pack()

master = Tk()
master.title('Hill Cipher Encryption and Decryption')
master.minsize(500,500)

messageLabel= Label (text ="Your Message: ")
messageLabel.pack()
messageEntry= Entry()
messageEntry.pack()

EncryptMessageLabel= Label (text ="Encrypted Message: ")
EncryptMessageLabel.pack()

btn = Button (text = "Encrypt", command = clickEncrypt())
btn.pack()

master.mainloop()


