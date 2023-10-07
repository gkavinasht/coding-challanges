import random

def generate(rows, cols, colors):
    matrix = [[None] * cols for _ in range(rows)]

    for i in range(rows):
        for j in range(cols):
            if i == 0 and j == 0:
                number = random.randint(0, colors - 1)
            else:
                while True:
                    found = 0
                    number = random.randint(0, colors - 1)

                    for k in range(i):
                        if matrix[k][j] == number:
                            found += 1
                            break

                    for l in range(j):
                        if matrix[i][l] == number:
                            found += 1
                            break

                    if found == 0:
                        break

            matrix[i][j] = number

    print(matrix)

generate(3, 3, 3)