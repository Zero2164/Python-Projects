# ---------IMPORTED MODULES---------


# ---------VARIABLES---------
quiz_list = [
    {
        'id': 1,
        'question': 'What does CPU stand for?',
        'answer': 'Central Processing Unit',
        'hint': '******* ********** ****'
    },
    {
        'id': 2,
        'question': 'What does CPU stand for?',
        'answer': 'Central Processing Unit'
    }
]

question = quiz_list[0]['question']
correct_answer = quiz_list[0]['answer']
hint = quiz_list[0]['hint']
# ---------FUNCTIONS---------


def confirm_playing():
    playing = input('\nDo you want to play? (Y/N) ')
    if playing.lower() != 'y':
        quit()
    print('Okay, Let\'s Play!\n')


def quiz_answer_handler(question, correct_answer, hint):
    answer = input(question + ' (type answer OR type \'hint\'): ')

    def check_answer():
        if answer.lower() == correct_answer.lower():
            print('Correct!')
        else:
            print('Incorrect!')

    if answer.lower() == 'hint':
        print('The answer should be presented as: ' + hint)
        answer = input(question + '(type answer OR type \'hint\')? ')
        check_answer()
    else:
        check_answer()


# ---------CONSOLE OUTPUT---------
print('\nWelcome to my computer quiz!')
confirm_playing()
quiz_answer_handler(question, correct_answer, hint)
