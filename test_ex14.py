from ex14 import word_frequency, word_frequency_with_boundary

song = """ 
hello, hello, hello, hello, one, two, three.
goodbye, goodbye, goodbye, goodbye, three, four, five.
"""

def test_word_frequency():
    assert word_frequency(song) == (['hello', 'goodbye'], 4)

def test_word_frequency_with_boundary():
    assert word_frequency_with_boundary(song, 2) == [(['hello', 'goodbye'], 4), (['three'], 2)]