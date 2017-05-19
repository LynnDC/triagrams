"""Tests for trigrams funcitons"""
import pytest

PARAMS_TABLE = [
    (["seattle", "weather",
    "is", "crazy", "I", "am", "getting",
    "fat", "and", "I", "am", "so",
    "sleepy", "oh", "my", "god"], 5, 'am'),
    (["seattle", "weather",
    "is", "crazy", "I", "am", "getting",
    "fat", "and", "I", "am", "so",
    "sleepy", "oh", "my", "god"], 4, "I"),
    (["seattle", "weather",
    "is", "crazy", "I", "am", "getting",
    "fat", "and", "I", "am", "so",
    "sleepy", "oh", "my", "god"], 3, 'crazy'),
    (["seattle", "weather",
    "is", "crazy", "I", "am", "getting",
    "fat", "and", "I", "am", "so",
    "sleepy", "oh", "my", "god"], 6, ["getting", "so"]),
]


@pytest.mark.parametrize('l, m, result', PARAMS_TABLE)
def test_parse_words(l, m, result):
    """test if our function will return a dictionary with 2 word key and a list or string value"""
    from trigrams import parse_words
    a = (' ').join(l[m - 2:m])
    b = result
    c = parse_words(l)
    assert c[a] == b


def test_generate_article():
    """Test if generate_article gives a valid list of strings."""
    from trigrams import generate_article, parse_words
    with open('sherlock.txt') as sherlock:
        result = parse_words(sherlock.read().split())
    list_of_words = generate_article(result, 10)
    assert len(list_of_words) == 10