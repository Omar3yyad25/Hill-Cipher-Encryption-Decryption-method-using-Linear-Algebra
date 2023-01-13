import tkinter
from crypt import *
from decrypt import *
from tkinter import *


def clickEncrypt():

   result = Label (text ="The encrypted message is:" + encrypt(messageEntry.get()))
   result.pack()

def clickDecrypt():
   result = Label (text ="The Original message is:" + decyrpt(DecyrptmessageEntry.get()))
   result.pack()


master = Tk()
master.title('Hill Cipher Encryption and Decryption')
master.minsize(500,500)

messageLabel= Label (text ="Your Message: ")
messageLabel.pack()
messageEntry= Entry()
messageEntry.pack()

btn1 = Button (text = "Encrypt", command = clickEncrypt)
btn1.pack()

DecryptmessageLabel= Label (text ="Encrypted Message: ")
DecryptmessageLabel.pack()
DecyrptmessageEntry= Entry()
DecyrptmessageEntry.pack()

btn2 = Button (text = "Decrypt", command = clickDecrypt)
btn2.pack()

master.mainloop()



#####################################################################################
##############  This code made by / Omar Ayyad & Mohamed Essam  #####################
#####################################################################################

