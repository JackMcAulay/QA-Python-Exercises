from itertools import combinations


def find_words(all_words, letters):
    words = []
    for i in range(0, len(letters) + 1):
        for subset in combinations(letters, i):
            if ''.join(subset) + '\n' in all_words:
                words.append(''.join(subset))
    return words


words_file = open('wordlist.txt', 'r')
words_list = words_file.readlines()
print(find_words(words_list, ['p', 'o', 't', 'n', 'i', 'e', 'b', 'u', 's']))
words_file.close()
