
class Console():

    def intro(self):
        print(
        '''
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        ~  Wilkommen zu dem Schere--Stein--Papier Spiel  ~
        ~  Shere --> 1                                   ~
        ~  Stein --> 2                                   ~
        ~  Papier --> 3                                  ~
        ~  Viel Gluck!                                   ~
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        ''')

    def functionality(self):
        print(
        '''
        Bitte schreiben Sie die Option:
        ''')

    def win(self):
        print(
        '''
                                :)
        Du hast gewonnen, Glückwunsch!
        Für eine neue Runde drücken Sie 9 für Exit drucken Sie 10
        ''')

    def lose(self):
        print(
        '''
                                :(
        Du hast nicht gewonnen, Versuchen Sie es das nächste Mal!
        Für eine neue Runde drücken Sie 9, für Exit drucken Sie 10
        ''')

    def calc_choise(self, arg1):
        print(f"Der Computer Auswahl: {arg1}")

    def user_choise(self,arg2):
        print(f"Deine Auswahl: {arg2}")

    def mesaj_iesire(self):
        print(
            'Danke fur dein Spiel, Schone Tag, Tschuss!!!'
        )



