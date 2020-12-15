import data
import utils

word = utils.get_random_word(data.words)
chars = []
score = 0

pseudo = input('Your pseudo ? ')

last_core = utils.get_last_scores(pseudo)

if last_core:
    print('Last score : ' + str(last_core))

while True:
    hidden_word = utils.generate_hidden_word(word, chars)

    print('hit ' + str(score) + '/' + str(data.nbMaxHit))
    print('Hidden word : ' + hidden_word)

    char = utils.get_input()
    chars.append(char)

    score += 1

    if score > data.nbMaxHit:
        print('The hidden word is : ' + word)
        print('DEFEATE !!!')
        break

    if utils.word_contains_in_chars(chars, word):
        utils.save_score(pseudo, score)
        print('The hidden word is : ' + word)
        print('VICTORY !!!')
        break
