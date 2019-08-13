from hangman import is_word_guessed, in_secret_word, get_available_letters, get_guessed_word

def test_is_word_guessed():
    secret_word = 'apple'
    letters_guessed = ['a','e','i','p','l']
    assert is_word_guessed(secret_word, letters_guessed) == True

def test_get_guessed_word():
    assert get_guessed_word("monkey", ['m', 'n', 'k', 'y']) == "m_ nk_ y"

def test_get_available_letters():
    assert get_available_letters(['m', 'n', 'k', 'y']) == "abcdefghijlopqrstuvwxz"