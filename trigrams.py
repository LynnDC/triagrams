"""Makes a set of trigrams to create a new body of text
    provided text file."""
import io


def main(file, x):
    """Opens file, splits it, grabs the desired chunk
        and makes a dictionary out of the words"""
    with io.open(file, encoding='utf=8') as test:
        text = test.read().split()
    # Logic goes here to remove undesired characters
    text_dict = {}
    for i in range(len(text) - x + 2):
        two_words = (' ').join(text[i: i + 2])
        third_word = text[i + 2]
        text_dict.setdefault(two_words, third_word)
    return text_dict
