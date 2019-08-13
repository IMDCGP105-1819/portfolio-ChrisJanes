import string

def is_word_guessed(secret_word, letters_guessed):
    correct = 0
    for letter in secret_word:
        if letter in letters_guessed:
            correct += 1

    return correct == len(secret_word)

def get_guessed_word(secret_word, letters_guessed):
    ret = ''

    for letter in secret_word:
        if letter in letters_guessed:
            ret += letter
        else:
            ret += '_ '

    return ret

def get_available_letters(letters_guessed):
    ret = ''

    for letter in string.ascii_lowercase:
        if letter not in letters_guessed:
            ret += letter

    return ret

print(is_word_guessed("monkey", ['m', 'o', 'n', 'k', 'e', 'y']))
print(get_guessed_word("monkey", ['m', 'n', 'k', 'y']))
print(get_available_letters(['m', 'n', 'k', 'y']))