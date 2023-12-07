# Here, I will perform a brute force attack an encrypted message
# to show why simple ciphers shouldn't be used!

"ks gvozz ohhoqy hvsa tfca hvs tfcbh oh bccb cb Tisgrom"

# first, I define the decrypt function
def cipher_decrypt_lower(ciphertext, key):

    decrypted = ""

    for c in ciphertext:

        if c.islower():

            c_index = ord(c) - ord('a')

            c_og_pos = (c_index - key) % 26 + ord('a')

            c_og = chr(c_og_pos)

            decrypted += c_og

        else:

            decrypted += c

    return decrypted

# next, I use "i" as a range of values between 0 and 26 for my brute force attack

cryptic_text = "ks gvozz ohhoqy hvsa tfca hvs tfcbh oh bccb cb Tisgrom"

for i in range(0,26):

    plain_text = cipher_decrypt_lower(cryptic_text, i)

    print("For key {}, decrypted text: {}".format(i, plain_text))