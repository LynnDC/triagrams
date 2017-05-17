"""Makes a set of trigrams to create a new body of text
    provided text file."""
import io


def main(file, x):
    """Opens file, splits it, grabs the desired chunk
        and makes a dictionary out of the words"""
    with io.open(file, encoding='utf=8') as test:
        text = test.read()

    text_split_by_spaces = text.split(' ')
    text_chunk = text_split_by_spaces[:x]
    # Logic goes here to remove undesired characters
    text_dict = {}
    for i in len(range(text_chunk) - 1):
        text_dict.update(dict((' ').join(text_chunk[:][i],
        text_chunk[:][i + 1]), text_chunk[:][i + 2]))
    return text_dict
