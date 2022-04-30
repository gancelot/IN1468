import sys

def read_words(filename='data.txt'):
    total_words = []
    try:
        with open(filename, encoding='utf8') as f:
            for line in f:
                line_words = line.strip().split()
                total_words.extend(line_words)
    except IOError as err:
        print(err, file=sys.stderr)

    return total_words

for word in read_words():
    print(word)

print('Generator version....')
# ---------------------------------------------------------------
# Generator version of the above code


def read_words_generator(filename='data.txt'):
    try:
        with open(filename, encoding='utf8') as f:
            for line in f:
                line_words = line.strip().split()
                for one_word in line_words:
                    yield one_word
    except IOError as err:
        print(err, file=sys.stderr)

for word in read_words_generator():
    print(word)
