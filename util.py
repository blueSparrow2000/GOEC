import random


def random_success(prob):  # prob is a float between 0~1 (probability of success)
    u = random.uniform(0, 1)
    return u <= prob  # because 'u<=prob' with probability 'prob'


def randomtext():
    texts = ["Ahh... I want a cup of tea...", "Does this cave have an exit..?", "I'm so tired...",
             "What is that?!... Oh... it was nothing.", "Thirsty...", "...", ""]
    return random.choice(texts)


def random_greetings():
    greetings = ['Hello', 'Welcome', 'Nice to meet', 'Good morning', 'Good evening', 'Bonjour', 'Hola', 'Buenos dias',
                 'Buenas tardes', '你好', '안녕하세요', '환영합니다']
    return random.choice(greetings)


def ask_player(question, answers):
    user_input = ''
    while user_input not in answers:
        print('{}'.format(question))
        answerstring = ''
        for answer in answers:
            answerstring = answerstring + answer + '/ '

        answerstring = answerstring[:-2]
        user_input = input('Select {}: '.format(answerstring)).upper()

    return user_input


def ask_language():
    lang_selection = {'1': 'Korean', '2': 'English'}
    languages = list(lang_selection.values())
    print("Select language: ")
    hotkeys = list(lang_selection.keys())
    print("{}: {}\n{}: {}".format(hotkeys[0], lang_selection[hotkeys[0]], hotkeys[1], lang_selection[hotkeys[1]]))
    user_input = ''
    while user_input not in ['1', '2']:
        user_input = input("Select (1 or 2): ")
    print('=' * 70)
    return lang_selection[user_input]
