"""Makes a set of trigrams to create a new body of text
provided text file.
"""


import io
import random
import sys


def main(doc, x): # pragma: no cover
    """Open file, splits it, grabs the desired chunk
        and makes a dictionary out of the words.
    """
    with io.open(doc, encoding='utf-8') as open_file:
        text = open_file.read().split()
    text_dict = parse_words(text)
    if x == 0:
        return None
    if x == 1:
        print(random.choice(text))
        return None
    else:
        generated_article = generate_article(text_dict, x)
        print(' '.join(generated_article))


def parse_words(words):
    """Parse the text list into a dictionary.
    """
    text_dict = {}
    for i in range(len(words) - 2):
        two_words = (' ').join(words[i: i + 2])
        third_word = words[i + 2]
        if two_words in text_dict.keys():
            if not isinstance(text_dict[two_words], list):
                text_dict[two_words] = [text_dict[two_words]]
            text_dict[two_words].append(third_word)
        else:
            text_dict.setdefault(two_words, third_word)
    return text_dict

def generate_article(dicty, x):
    """Generate a paragraph from startings words
    and our dictionary from parse_words.
    """
    paragraph = []
    text_key = random.choice(list(dicty.keys()))
    paragraph.extend(text_key.split())
    for _ in range(0, x-2):
        text_key = ' '.join(paragraph[-2:])
        if isinstance(dicty[text_key], list):
            paragraph.append(random.choice(dicty[text_key]))
        else:
            paragraph.append(dicty[text_key])
    return paragraph

if __name__ == '__main__':
    main(str(sys.argv[1]), int(sys.argv[2]))
