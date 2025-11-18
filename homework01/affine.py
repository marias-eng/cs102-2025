def encrypt_affine(plaintext: str, a: int, b: int) -> str:
    """
    Encrypts plaintext using an Affine cipher.
    """
    ciphertext = ""
    rus_alphabet_size = 32  # количество символов в русском алфавите без учета буквы ё
    a_num = ord("а")
    A_num = ord("А")
    text_to_encrypt = plaintext.replace("Ё", "Е").replace("ё", "е")
    for char in text_to_encrypt:
        if "А" <= char <= "Я":
            size = A_num
        elif "а" <= char <= "я":
            size = a_num
        else:
            ciphertext += char
            continue
        x = ord(char) - size
        encrypted_position = (a * x + b) % rus_alphabet_size
        ciphertext += chr(encrypted_position + size)
    return ciphertext
