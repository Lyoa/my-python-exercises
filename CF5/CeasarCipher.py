def encrypt(text,shift_amount):
    result = ""

    for i in range(len(text)):
        letter = text[i]
        if ord(letter) >= 65 and ord(letter) <= 90:
            result += chr((ord(letter) + shift_amount - 65) % 26 + 65)
        elif ord(letter) >= 97 and ord(letter) <= 122:
            result += chr((ord(letter) + shift_amount - 97) % 26 + 97)
        else:
            result += letter

    return result

text = input("Enter the word to be decoded: ")
shift_amount = int(input("Enter the shift amount: "))

print(encrypt(text,shift_amount))

