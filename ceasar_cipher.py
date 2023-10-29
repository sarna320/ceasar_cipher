from ceasar_cipher_alphabet import alphabet
from ceasar_cipher_art import logo


def encrypt(text_, shift_):
    encrypted = ""
    for i in range(0, len(text_)):
        if ord(text_[i])>=97 and ord(text_[i])<=122: 
            if alphabet.index(text_[i]) + shift_ <= 25:
                encrypted += alphabet[alphabet.index(text_[i]) + shift_]
            else:
                encrypted += alphabet[alphabet.index(text_[i]) + shift_ - 26]
        else:
            encrypted+=text_[i]
    print(encrypted)


def decrypt(text_, shift_):
    encrypted = ""
    for i in range(0, len(text_)):
        if ord(text_[i])>=97 and ord(text_[i])<=122: 
            if alphabet.index(text_[i]) - shift_ < 0:
                encrypted += alphabet[alphabet.index(text_[i]) - shift_ + 26]
            else:
                encrypted += alphabet[alphabet.index(text_[i]) - shift_]
        else:
            encrypted+=text_[i]
    print(encrypted)


def caesar(text_, shift_, direction_):
    shift_=shift_%26
    if direction_ == "encode":
        encrypt(text_, shift_)
    elif direction_ == "decode":
        decrypt(text_, shift_)


print(logo)
restart="yes"
while(restart=="yes"):
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(text, shift, direction)
    restart=input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")