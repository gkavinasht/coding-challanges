"""
Given the length of a word and maximum number of consecutive vowels that it can contain, determine how many unique words can be generated. words will consists of a to z alphabets and vowels contains {a, e, i, o, u}.

example:
wordlen = 1
maxVowels = 1
That means there are 26 possibilities, one for each letter in the alphabet
"""

def count_unique_words(word_len, max_vowels):
    vowels = {'a', 'e', 'i', 'o', 'u'}

    def generate_words(word, consecutive_vowels):
        if len(word) == word_len:
            return 1

        count = 0
        for char in 'abcdefghijklmnopqrstuvwxyz':
            if char in vowels:
                if consecutive_vowels < max_vowels:
                    count += generate_words(word + char, consecutive_vowels + 1)
                else:
                    continue
            else:
                count += generate_words(word + char, 0)

        return count

    return generate_words('', 0)

# Example usage:
word_len1, max_vowels1 = 1, 1
result1 = count_unique_words(word_len1, max_vowels1)
print(result1)  # Output: 26

word_len2, max_vowels2 = 4, 1
result2 = count_unique_words(word_len2, max_vowels2)
print(result2)  # Output: 412776