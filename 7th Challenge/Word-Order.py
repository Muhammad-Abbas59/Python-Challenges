from collections import OrderedDict

def word_occurrences(n, words):
    word_count = OrderedDict()

    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    distinct_words_count = len(word_count)
    occurrences_count = list(word_count.values())

    print(distinct_words_count)
    print(*occurrences_count)

if __name__ == '__main__':
    n = int(input().strip())
    words = [input().strip() for _ in range(n)]

    word_occurrences(n, words)
