matrixSize = int(input("수 입력 : "))

matrixArr = [[0 for j in range(matrixSize)] for i in range(matrixSize)]
num = 0
x = -1
y = 0


def snail(arrNum, num, checkSize, m, n, direct):
    if(checkSize == 0):
        return
    for i in range(2*checkSize - 1):
        if(i < checkSize):
            m = m + direct
        else:
            n = n + direct

        num = num + 1
        arrNum[n][m] = num
    snail(arrNum, num, checkSize - 1, m, n, direct * (-1))

snail(matrixArr, num, matrixSize,x, y, 1)

for i in range(matrixSize):
    print(matrixArr[i])