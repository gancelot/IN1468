"""
    26_reduce_example.py
    Using reduce()
"""
import functools


def sentence_maker(word1, word2):
    return ' '.join([word1, word2])

results = functools.reduce(sentence_maker, ['Four', 'score', 'and', 'seven', 'years', 'ago'])
print(results)