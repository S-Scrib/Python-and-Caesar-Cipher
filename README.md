# Python-and-Caesar-Cipher
Just some fun making a caesar cipher for plain text, numbers/special characters, and files. for funsies, made a brute force attack on the cipher to show why it shouldn't be used!
Shoutout to likegeeks.com for this one. Was a fun project and tutorial!

The whole idea of the Caesar cipher started way back in 100 BC. It was used by Julius Caesar to send secret messages out to his various gnerals in the field. The cipher "shifted" letters three spaces. Example being A would turn to D and B would E. This shift became known as a "shift cipher". Today, instead of using a shift of 3, we use "ROT 13". ROT 13 stands for 'rotate by 13 places'. Basically, A would be beome N and so on. It is used a lot to hide spoilers for media like movies and TV shows. Good for hiding infor at a quick glance, but can be easily broken by frequency analysis or a brute force attack for those inclined to put in the effort. Anyways...what I did in each file is below:

# ENCRYPTION:
So for the Encryption File, I used the ord() function to convert characters in numeric representation in Unicode. I then used the chr() function to find a character that is represented by a number:



<img width="466" alt="image" src="https://github.com/S-Scrib/Python-and-Caesar-Cipher/assets/152911365/7fe382fe-b8fc-4794-ad5b-c5a8425e5fb2">

After that, I provided the shift I wanted and the text I wanted encrypted:


<img width="128" alt="image" src="https://github.com/S-Scrib/Python-and-Caesar-Cipher/assets/152911365/537d1fc7-3c21-44dc-98e1-bf91634e48ab">

Now the fun part! I wanted to shift only capital letters for this, so wanted to check the message for uppercase letters and covert those to a new letter based on the shift value of 3:


<img width="325" alt="image" src="https://github.com/S-Scrib/Python-and-Caesar-Cipher/assets/152911365/a3dd9457-f924-4ab7-bf44-677815f754b6">

If it was a lower case letter, I left it alone using the below:


<img width="290" alt="image" src="https://github.com/S-Scrib/Python-and-Caesar-Cipher/assets/152911365/ff5fb4c8-d671-4b8d-9ab6-f7250e05d3b2">

Lastly, I ran the script using below:


<img width="308" alt="image" src="https://github.com/S-Scrib/Python-and-Caesar-Cipher/assets/152911365/0428a45d-d53d-4608-8099-a44a27f7ad4b">

And if I did it right, the capital letters should be shifted 3 spots to the right. 


<img width="150" alt="image" src="https://github.com/S-Scrib/Python-and-Caesar-Cipher/assets/152911365/94ea3fed-e5c6-447a-9445-26d670101397">


It Works! Hail Caesar!

# DECRYPTION:
