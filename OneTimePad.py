def otpEncryption(plainText: str, key: str) -> str:
    cipherText = ""
    for i in range(len(plainText)):
        cipherText += str((int(plainText[i]) + int(key[i]))%10)
    return cipherText
