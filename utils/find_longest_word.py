def find_longest_word(words):
    longest_word, _= max(words, key=lambda x: x[1])
    return longest_word