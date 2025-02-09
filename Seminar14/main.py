def Autokennzeichnen(string:str):
    jud = ['CJ','MM','SB','B']
    text_imprtit = string.split('-')
    if len(text_imprtit) != 3:
        return False
    if text_imprtit[0] not in jud:
        return False
    if not text_imprtit[1].isdigit() and (len(text_imprtit[1]) == 2 or len(text_imprtit[1] == 3)):
        return False
    if len(text_imprtit[2]) != 3 or not text_imprtit[2].isalpha():
        return False
    return True


def pig_latin():
    f = open("data.in",'r')
    satze = f.read().split(',')
    f.close()
    for s in satze:
        words = s.split(' ')
        # for word in words:
        #     n_w = word[1:] + word[0] + 'ay'
        #     print(n_w)
        new_words = list(map(lambda x: x[1:] + x[0] + 'ay',words))
        print(' '.join(new_words))




# print(Autokennzeichnen('CJ-25-FJA')
pig_latin()


