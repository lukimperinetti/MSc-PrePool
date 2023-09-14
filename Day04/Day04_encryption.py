# ----- Encryption ----- #

def encrypt(msg):
    i = []
    # ord renvoi valeur ascii
    for x in msg:
        if x.isalpha():  # Vérifiez si le caractère est alphabétique
            ascii_val = ord(x)
            shifted_ascii = (ascii_val - 97 + 4) % 26 + 97  # Incrémentation avec gestion du passage à 97
            i.append(shifted_ascii)
        else:
            i.append(ord(x))  # Si ce n'est pas une lettre, ajoutez le code ASCII tel quel

    result_string = "".join(chr(ascii_val) for ascii_val in i)
    print(result_string)

msg = input('Votre message >> ')
# encrypt(msg)

def decrypt(msg):
    i = []
    # ord renvoi valeur ascii
    for x in msg:
        if x.isalpha():  # Vérifiez si le caractère est alphabétique
            ascii_val = ord(x)
            shifted_ascii = (ascii_val - 97 - 4) % 26 + 97  # Incrémentation avec gestion du passage à 97
            i.append(shifted_ascii)
        else:
            i.append(ord(x))  # Si ce n'est pas une lettre, ajoutez le code ASCII tel quel

    result_string = "".join(chr(ascii_val) for ascii_val in i)
    print(result_string)

msg = input('Votre message >> ')
decrypt(msg)