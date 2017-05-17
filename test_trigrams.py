
def test_trigrams():
    """test trigrams function"""
    from trigrams import main
    assert main(text.txt, 6) == {"seattle weather": "is", "weather is":"crazy,", "is crazy,": "I", "crazy, I": "need"}

