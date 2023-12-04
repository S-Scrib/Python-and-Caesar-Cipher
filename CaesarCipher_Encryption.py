# Mathematical Expression for Caesar Cipher encryption rule
# c = (x + n) % 26

# I use the ord() function to convert a character into numeric representation in Unicode
c_unicode = ord("c")

A_unicode = ord("A")

print("Unicode of 'c' =", c_unicode)

print("Unicode of 'A' =", A_unicode)

# Here, I use the chr() function to find the character that is represented by a number. Basically, the inverse of
# the ord() function

character_65 = chr(65)

character_100 = chr(100)

print("Unicode 65 represents", character_65)

print("Unicode 100 represents", character_100)

character_360 = chr(360)

print("Unicode 360 represents", character_360)

# OK, cool...methods have been introduced. Now, I'm going to implement the encryption technique for capital letters
# only. lower case will be left alone.
# First, I define the shift value of caesar cipher

shift = 3
text = "Hello World"
encryption = ""

for c in text:

    # this is to check if character is an uppercase letter

    if c.isupper():

        # I use the 2 lines below to find positions from 0-25
        c_unicode = ord(c)
        c_index = ord(c) - ord("A")

        # now I use the formula above to execute the shift
        new_index = (c_index + shift) % 26

        # ok, now im converting to a new character
        new_unicode = new_index + ord("A")
        new_character = chr(new_unicode)

        # Now I am appending the encrypted string
        encryption = encryption + new_character

    else:
        # this part is saying if not uppercase, leave it as is
        encryption += c

print("Plain text:", text)
print("Encrypted text:", encryption)

# The H and W are now shifted three spots on the alphabet to K and Z!
