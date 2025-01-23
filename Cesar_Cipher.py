alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n",
            "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n",
            "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
direction = input("Enter Encode for Encrypting OR Decode for Decrypting:\n").lower()
text = input("Enter the Text:\n").lower()
shift = input("Enter the shift:")

def encrypt(t, s):
  cipher = ""
  for letter in t:
    position = alphabet.index(letter)
    new_position = int(position) + s
    new_letter = alphabet[new_position]
    cipher += new_letter
  print(f"The Encrypted code is {cipher}")

def decrypt(t, s):
  cipher = ""
  for letter in t:
    position = alphabet.index(letter)
    new_position = int(position) - s
    new_letter = alphabet[new_position]
    cipher += new_letter
  print(f"The Decrypted code is {cipher}")

if direction == "encode":
  encrypt(t, s)
if direction == "decode":
  decrypt(t, s)
