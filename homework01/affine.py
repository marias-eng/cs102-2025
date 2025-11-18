def encrypt_affine(plaintext: str, a: int, b: int) -> str:
    """
    Шифрует текст с помощью аффинного шифра на русском алфавите.
    """
    rus_alph_size = 32  # количество букв в русском алфавите без ё
    text_to_encrypt = plaintext.replace("Ё", "Е").replace("ё", "е")
    ciphertext = ""
    for char in text_to_encrypt:
        if "А" <= char <= "Я":
            size = ord("А")
        elif "а" <= char <= "я":
            size = ord("а")
        else:
            ciphertext += char
            continue
        x = ord(char) - size
        encrypted_position = (a * x + b) % rus_alph_size
        ciphertext += chr(encrypted_position + size)

    return ciphertext
