alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


# def encrypt(text, shift):
#   encryption = ""
#   for char in text:
#    alphabet_index = alphabet.index(char)
#    encryption += alphabet[alphabet_index + shift]

#   print(f"The encoded text is {encryption}")

# def decrypt(text, shift):
#   decryption = ""
#   for char in text:
#    alphabet_index = alphabet.index(char)
#    decryption += alphabet[alphabet_index - shift]

#   print(f"The decoded text is {decryption}")

def caesar(text, shift):
  mystery_word = ""
  for char in text:
    alphabet_index = alphabet.index(char)
    if direction == 'encode':
      mystery_word += alphabet[alphabet_index + shift]
    elif direction == 'decode':
      mystery_word += alphabet[alphabet_index - shift]
  print(f"The new message is {mystery_word}")

caesar(text = text, shift = shift)