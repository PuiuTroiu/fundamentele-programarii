from repository.state import get_current_state
def guess(word,choise,current_state):
    '''
    builds a state based in the choise of the user
    word: what to guess
    param: character
    return: state as a Tuple
    '''
    new_state = ()
    guessed = 0
    guessed_indexes = []
    current_guessed_indexes = current_state[2]

    found = False

    for index in range(len(word)):
        if choise == word[index] and index not in current_guessed_indexes:
            guessed_indexes.append(index)
            found = True

    tries = 1 if not found else 0
    guessed = 1 if found else 0
    return current_state[0] + tries,current_state[1]+guessed,current_state[2]+guessed_indexes


def win(states,word,Max_tries):
    if len(get_current_state(states)[2]) == len(word):
        return True


    # if get_current_state(states)[0] > Max_tries:
    #     return False