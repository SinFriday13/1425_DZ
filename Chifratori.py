from Crypto.Cipher import AES, DES, DES3
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

def encrypt_AES():
    key = get_random_bytes(32)  # Генерация ключа (16, 24 или 32 байта для AES)
    cipher = AES.new(key, AES.MODE_CBC)  # Создание объекта шифрования
    ciphertext = cipher.encrypt(pad(message, AES.block_size))  # Шифрование
    print('Ключ: ', key.hex())
    print("Зашифрованные данные:", ciphertext.hex())
    print("IV (вектор инициализации):", cipher.iv.hex())

def decrypt_AES():
    iv = bytes.fromhex(input("Введите IV (вектор инициализации): "))
    cipher = AES.new(key, AES.MODE_CBC, iv=iv)
    plaintext = unpad(cipher.decrypt(bytes.fromhex(message)), AES.block_size)
    print("Расшифрованные данные:", plaintext.decode())

def encrypt_DES():
    key = get_random_bytes(8)  # Генерация ключа (8 байт для DES)
    cipher = DES.new(key, DES.MODE_ECB)  # Создание объекта шифрования
    ciphertext = cipher.encrypt(pad(message, DES.block_size))  # Шифрование
    print('Ключ: ', key.hex())
    print("Зашифрованные данные:", ciphertext.hex())

def decrypt_DES():
    cipher = DES.new(key, DES.MODE_ECB)
    plaintext = unpad(cipher.decrypt(bytes.fromhex(message)), DES.block_size)
    print("Расшифрованные данные:", plaintext.decode())

def encrypt_Triple_DES():
    key = get_random_bytes(24)  # Генерация ключа (16 или 24 байта для Triple DES)
    cipher = DES3.new(key, DES3.MODE_ECB)  # Создание объекта шифрования
    ciphertext = cipher.encrypt(pad(message, DES3.block_size))  # Шифрование
    print('Ключ: ', key.hex())
    print("Зашифрованные данные:", ciphertext.hex())

def decrypt_Triple_DES():
    cipher = DES3.new(key, DES3.MODE_ECB)
    plaintext = unpad(cipher.decrypt(bytes.fromhex(message)), DES3.block_size)
    print("Расшифрованные данные:", plaintext.decode())


action = int(input('1 - Зашифровать\n2 - Расшифровать\nВыберите действие: '))
tip = int(input("Введите тип шифрования: \nAES - 1\nDES - 2\nTriple DES - 3\nВведите число: "))

if action == 1:
    message = input("Введите сообщение: ").encode('utf-8')  # Данные для шифрования
elif action == 2:
    key = bytes.fromhex(input('Введите ключ: '))
    message = input("Введите зашифрованное сообщение: ")  # Данные для расшифрования
else:
    print('Неизвестное действие')
    exit()

if tip == 1:
    if action == 1:
        encrypt_AES()
    elif action == 2:
        decrypt_AES()
elif tip == 2:
    if action == 1:
        encrypt_DES()
    elif action == 2:
        decrypt_DES()
elif tip == 3:
    if action == 1:
        encrypt_Triple_DES()
    elif action == 2:
        decrypt_Triple_DES()
else:
    print('Неизвестный тип шифрования')
