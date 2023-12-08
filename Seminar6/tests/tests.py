from logik.hangman import guess
def test_guess():
    '''
    masina
    state(nr of tries,guessed,guessed_position)
    state la start:(0,0,[])

    choise = S:(0,1,[2])

    choise - N:(0,2,[2,4])

    choise = X:(1,2,[2,4])

    '''

    assert guess('masina','s',(0,0,[])) == (0,1,[2])
    assert guess('masina','i',(0,1,[1,5])) == (0,2,[1,5,3])