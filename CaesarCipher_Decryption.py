# Ok, now to decipher -- here is the formular again: c = (x + n) % 26
# This time, let's use a NEGATIVE shift

shift = 3
encrypted_text = "Kello Zorld"
plain_text = ""

for c in encrypted_text:

    if c.isupper():

        # again, finding positions 0-25
        c_unicode = ord(c)
        c_index = ord(c) - ord("A")

        # Here, in the formular, I apply a NEGATIVE shift to decrypt the message!
        new_index = (c_index - shift) % 26

        # now covert to the new characters as we did with encryption
        new_unicode = new_index + ord("A")
        new_character = chr(new_unicode)

        # Now I append the plain string
        plain_text = plain_text + new_character

    else:
        # Again, define that lower case letters are to be left alone
        plain_text += c

print("Encrypted text:", encrypted_text)
print("Decrypted text:", plain_text)

# The encrypted text has now shifted back 3 spaces to display the original message
