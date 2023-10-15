text = input("Введите текст для шифрования: ")
shift = int(input("Введите сдвиг: "))
encrypted_text = ""
for char in text:
    if char.isalpha():
        shifted_char = chr((ord(char) - 65 + shift) % 26 + 65) if char.isupper() else chr((ord(char) - 97 + shift) % 26 + 97)
        encrypted_text += shifted_char
    else:
        encrypted_text += char
print("Зашифрованный текст:", encrypted_text)