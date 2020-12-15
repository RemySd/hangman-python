import random
import pickle
import data


def get_input() -> str:
    """Input player for a character with the check"""
    char = ''

    while len(char) != 1 and not char.isdigit():
        char = input('Your letter ? ')

    return char


def get_random_word(words: list) -> str:
    """Get a random word in words"""
    rnd_number = random.randint(0, len(words) - 1)

    return words[rnd_number]


def generate_hidden_word(word: str, char_not_hide: list) -> str:
    """
    Generate a string with *** for all character
    Example:
        orange => ******
        test => ****
    """
    final_word = ''
    for char in word:
        if char in char_not_hide:
            final_word += char
        else:
            final_word += '*'

    return final_word


def word_contains_in_chars(chars: list, word: str) -> bool:
    """check if the chars list contains all chars in word"""
    for char in list(word):
        if char not in chars:
            return False

    return True


def save_score(pseudo: str, score: int) -> None:
    try:
        score_storage = pickle.load(open(data.file_score_name, 'rb'))
    except (OSError, IOError) as e:
        score_storage = {pseudo: score}
        pickle.dump(score_storage, open(data.file_score_name, 'wb'))
        return

    score_storage[pseudo] = score
    pickle.dump(score_storage, open(data.file_score_name, 'wb'))


def get_last_scores(pseudo: str):
    try:
        scores = pickle.load(open(data.file_score_name, 'rb'))
        if scores.get(pseudo):
            return scores.get(pseudo)
    except (OSError, IOError) as e:
        return None

    return
