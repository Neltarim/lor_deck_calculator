from core.classes import Decks


class main():
    """ Main loop program """
    def __init__(self):
        self.decks = Decks()
        self.loop = True
        
        while self.loop == True:
            self.menu() #loop menu

    ##### menu loop ########

    def pick_option(self, options):
        """ Start the function selected by the user from the list in parameters """
        self.clear_screen() #print 100 lines
        i = 1 #use to know what function to start
        for option in options:
            print("{}. {}".format(i, option['desc'])) #print the description and 'id' of all func
            i += 1

        res = input("Tap the number of the option you want to go :")
        res = int(res)
        res -= 1 #because a list start at 0, not 1

        if res <= i-1 and res >= 0:
            self.clear_screen()
            options[res]['func']() #call the function
            self.wait()
        
        else:
            print("Wrong argument.")
            self.pick_option(options) #restart recursively


    def menu(self):
        """ Redirection function to pick option with options's payload """
        options = [
            {'desc': 'Deck list',      'func': self.decks.print_decks},
            {'desc': 'New deck',       'func': self.decks.add_deck},
            {'desc': 'Delete a deck',  'func': self.decks.delete_deck},
            {'desc': 'update jokers',  'func': self.decks.dump_jokers},
            {'desc': 'quit',           'func': exit}
        ]
        self.pick_option(options)

    def clear_screen(self):
        """ Clear the terminal """
        print("\n" * 100)

    def wait(self):
        """ Press ENTER to continue """
        input("press \"ENTER\" to continue ...")

if __name__ == "__main__":
    Main = main()
    Main.menu()