# Here, I make a Vigenere cipher. Basically, instead of single shifts...
# this cipher performs different shifts at different positions in the text by use of sequences of keys.

def vigenere_cipher(text, keys, decrypt=False):
    # vigenere cipher for lowercase letters
    n = len(keys)

    translatedText = ""

    i = 0  # used to record the count of lowercase characters processed so far

    # iterate over each character in the text
    for c in text:

        # translate only if c is lowercase
        if c.islower():

            shift = keys[i % n]  # decide which key is to be used

            if decrypt == True:
                # if decryption is to be performed, make the key negative
                shift = -shift

            # Perform the shift operation
            shifted_c = chr((ord(c) - ord('a') + shift) % 26 + ord('a'))

            translatedText += shifted_c

            i += 1

        else:

            translatedText += c

    return translatedText

text = "Let him not vow to walk in the dark, who has not seen the nightfall"

encrypted_text = vigenere_cipher(text, [1,2,3])

print("Plain text:\n", text)

print("Encrypted text:\n", encrypted_text)

