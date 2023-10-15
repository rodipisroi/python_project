from art import logo

alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

print(logo)

repeat = True
while repeat == True:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")

  # def encrypt(plain_text, shift_amount):
  #   ciphertext = ""
  #   for letter in plain_text:
  #      position = alphabet.index(letter)
  #      rotation = position + shift_amount
  #      if rotation >=26:
  #        new_position = rotation % 26
  #        new_letter = alphabet[new_position]
  #      else:
  #        new_letter = alphabet[rotation]
  #      ciphertext += new_letter
  #   print(f"The encrypted message is:\n{ciphertext}")

  # def decrypt(cipher_text, shift_amount):
  #   plaintext = ""
  #   for letter in cipher_text:
  #      position = alphabet.index(letter)
  #      rotation = position - shift_amount
  #      new_letter = alphabet[rotation]
  #      plaintext += new_letter
  #   print(f"The decrypted message is:\n{plaintext}")

  # if direction == "encode":
  #   text = input("Type your message:\n").lower()
  #   shift = int(input("Type the shift number:\n"))
  #   encrypt(plain_text=text, shift_amount=shift)
  # elif direction == "decode":
  #   text = input("Type your message:\n").lower()
  #   shift = int(input("Type the shift number:\n"))
  #   decrypt(cipher_text=text, shift_amount=shift)
  # else:
  #   print("Your command not valid")


  def caesar(type):
    if type == "encode" or type == "decode":
      text = input("Type your message:\n").lower()
      shift_amount = int(input("Choose your rotation number:\n"))
      convertion_text = ""
      for letter in text:
        if letter in alphabet:
          position = alphabet.index(letter)
          if type == "encode":
            rotation = position + shift_amount
            if rotation >= 26:
              rotate_convert = rotation % 26
              rotation = rotate_convert
          elif type == "decode":
            rotation = position - shift_amount
            if rotation <= -26:
              rotate_convert = rotation % 26
              rotation = rotate_convert
          new_letter = alphabet[rotation]
          convertion_text += new_letter
        else:
          convertion_text += letter
      print(f"The {type}d text is:\n{convertion_text}")
    else:
      print("Command is not valid")

  caesar(direction)
  askrepeat = input("Dou you want to repeat again? Type 'yes' or 'no'\n")
  if askrepeat == 'yes':
    repeat = True
  else:
    repeat = False
    print("The program has ended")
