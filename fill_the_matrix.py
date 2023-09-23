# Fill The Matrix
# Given a fixed-size matrix and a sentence represented by a list of strings, return the number of times the given sentence can be filled on the matrix.
# A single string should not be split into multiple rows.
# The order of the strings in the sentence remains unchanged.
# Each cell in the matrix should contain either a single character or a space.
# A single space must separate two consecutive strings in a line.

def fillMatrix(rows, cols, sentence):
    numberofTimes = 0
    r, c = 0, 0
    matrix = [["."] * (cols) for _ in range(rows)]

    while r < rows:
        wordCount = 0
        for word in sentence:
            if cols - c < len(word):
                r += 1
                c = 0
            for ch in word:
                if r in range(rows) and c in range(cols):
                    matrix[r][c] = ch
                    c += 1
                else:
                    return numberofTimes
            c += 1
            wordCount += 1
        if cols - c < len(word): 
            r += 1
            c = 0
        if wordCount == len(sentence):
            numberofTimes += 1

    return numberofTimes

rows = 8
cols = 5
sentence = ["abcd", "ef", "gh", "ijk", "l", "m"]

print(fillMatrix(rows, cols, sentence))

# Output: 2
# Given sentence can be filled twice on the screen of size 8 x 5:
# abcd.
# ef.gh
# ijk.l
# m....
# abcd.
# ef.gh
# ijk.l
# m....
# Assume dot(.) represents an empty space.

# Time Compelxity: O(rows * words * max_word_length)
# Space Complexity: O(rows * cols)