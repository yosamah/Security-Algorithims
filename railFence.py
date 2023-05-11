from typing import Set


def encryptRailFence(depth: int, message: str)-> str:

    railFenceArray = [ [-1]*depth for _ in range(len(message))]

    currentDepth: int = 0
    prevOperation: int = 0 # 0 inc & 1 dec
    for index in range(len(message)):
        railFenceArray[index][currentDepth] = message[index]
        if prevOperation == 0:
            currentDepth+=1
            if currentDepth == depth-1:
                prevOperation = 1
        else:
            currentDepth-=1
            if currentDepth == 0:
                prevOperation = 0

    cypherMessage: str = ""

    # Get transpose of matrix
    railFenceArray =[[row[i] for row in railFenceArray] for i in range(len(railFenceArray[0]))]
    for arr in railFenceArray:
        for character in arr:
            if character != -1:
                cypherMessage+= character
    return cypherMessage


message: str = "1223456712234"
print(encryptRailFence(3, message))
