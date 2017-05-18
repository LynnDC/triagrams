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
    # result = {"seattle weather": "is", "weather is": "crazy", "is crazy": "I", "I am": ["getting", "so"], "am getting": "fat", "fat and": "I", "so sleep": "oh", "oh my": "god"}
    a = (' ').join(l[m - 2:m])
    b = result
    c = parse_words(l)
    assert c[a] == b


def test