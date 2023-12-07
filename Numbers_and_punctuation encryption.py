# Ok, for this one I am trying to encrypt and decrypt numbers instead of letters.
# I am going to make a function that accepts the shift values
# Going to implement two functions: cipher_encrypt() and cipher_decrypt()

def cipher_encrypt(plain_text, key):

    encrypted = ""

    for c in plain_text:

        if c.isupper():

            c_index = ord(c) - ord('A')

            # here I am shifting the characters by key position.
            c_shifted = (c_index + key) % 26 + ord('A')
            c_new = chr(c_shifted)

            encrypted += c_new

        elif c.islower():

            # here I am subtracting the unicode of 'a' to get within the 0-25 range
            c_index = ord(c) - ord('a')
            c_shifted = (c_index + key) % 26 + ord('a')
            c_new = chr(c_shifted)

            encrypted += c_new

        elif c.isdigit():
            # the below is saying that if it is a number, it will shift its value
            c_new = (int(c) + key) % 10
            encrypted += str(c_new)

        else:
            # below states that if it is not a digit or letter, leave it be
            encrypted += c

    return encrypted

# ALERT: below starts the decryption function
# The Decryption function

def cipher_decrypt(ciphertext, key):

    decrypted = ""

    for c in ciphertext:

        if c.isupper():

            c_index = ord(c) - ord('A')

            # here is where I shift the characters back to obtain the original text

            c_og_pos = (c_index - key) % 26 + ord('A')

            c_og = chr(c_og_pos)

            decrypted += c_og

        elif c.islower():

            c_index = ord(c) - ord('a')

            c_og_pos = (c_index - key) % 26 + ord('a')

            c_og = chr(c_og_pos)

            decrypted += c_og

        elif c.isdigit():

            # Here, I apply the same principle I have with letters, but with digits
            c_og = (int(c) - key) % 10

            decrypted += str(c_og)

        else:

            # Here, I am applying anything that isn't a number or a letter to be left as is
            decrypted += c

    return decrypted

plain_text = " This message is encrypted. Do not share!"

ciphertext = cipher_encrypt(plain_text, 4)
print("Plain text message:\n", plain_text)
print("Encrypted ciphertext:\n", ciphertext)

# here I decrypted the now encrypted message

ciphertext = "Xlmw qiwweki mw irgvctxih. Hs rsx wlevi!"

decrypted_msg = cipher_decrypt(ciphertext, 4)

print("The cipher text:\n", ciphertext)

print("The decrypted message is:\n",decrypted_msg)

