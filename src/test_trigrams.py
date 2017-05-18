"Tests for trigrams funcitons"
import pytest


def test_parse_words():
    """test if our function will return a dictionary with 2 word key and a list or string value"""
    from trigrams import parse_words
    my_words = ["seattle", "weather", "is", "crazy", "I", "am", "getting", "fat", "and", "I", "am", "so", "sleepy", "oh", "my", "god"]
    # result = {"seattle weather": "is", "weather is": "crazy", "is crazy": "I", "I am": ["getting", "so"], "am getting": "fat", "fat and": "I", "so sleep": "oh", "oh my": "god"}
    a = (' ').join(my_words[: 2])
    b = my_words[2]
    c = parse_words(my_words)
    assert c[a] == b

