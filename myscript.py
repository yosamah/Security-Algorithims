def vignereDecryption(plainText: str, CiphterText: str) -> str:
    plainText = plainText.upper()
    CiphterText = CiphterText.upper()
    key = ""
    for i in range(len(plainText)):
        key += chr((ord(CiphterText[i]) - ord(plainText[i]) + 26) % 26 + ord("A"))
    return key

print(vignereDecryption("EABRGIGDH","COMPUTERS"))