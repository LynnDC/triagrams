import pytest


def test_trigrams():
    """test trigrams function"""
    from trigrams import main
    is_dict = main('text.txt', 4)
    assert isinstance(is_dict, dict)
    assert len(is_dict) == 17
