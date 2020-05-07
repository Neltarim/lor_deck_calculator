import pickle

from core.const import *


class Decks():
    
    def __init__(self):
        self.all = self.get_decks()
        self.jokers = self.get_jokers()
        self.temp = None

    def dump_jokers(self):
        self.print_jokers()
        print("Enter the new values :\n")

        for joker in self.jokers:
            res = input(joker + " :")
            self.jokers[joker] = res
            
        with open(JOKERS_PICKLE, "wb") as file:
            pickler = pickle.Pickler(file)
            pickler.dump(self.jokers)

        print("Jokers successfuly added.")

        self.update_decks()
            

    def get_jokers(self):
        with open(JOKERS_PICKLE, "rb") as file:
            unpickler = pickle.Unpickler(file)

            jokers = unpickler.load()

        return jokers

    def print_jokers(self):
        jokers = self.get_jokers()

        print("Jokers in your hands :")

        print(" ------------------------------------------------------------")
        for joker in jokers:
            print("| {} : {} | ".format(joker, jokers[joker]), end="")

        print("\n ------------------------------------------------------------\n\n")

    def print_decks(self):
        self.print_jokers()
        print("Your next decks to shine in ranked :")
        decks = self.get_decks()

        i = 1
        for deck in decks:
            print("_____________________________________________________________\n")
            print("{}. {} :\n".format(i, deck['name']))
            i += 1

            print("- Champions:   {}".format(deck['champions']))
            print("- Epics:       {}".format(deck['purples']))
            print("- Rares:       {}".format(deck['blues']))
            print("- Commons:     {}\n".format(deck['greens']))

            print("Total without jokers:    {}".format(deck['total_without']))
            print("Total with jokers:       {}".format(deck['total_with']))
            print("_____________________________________________________________\n\n")

    def get_decks(self):
        with open(DECKS_PICKLE, "rb") as file:
            unpickler = pickle.Unpickler(file)

            decks = unpickler.load()

        return decks

    def dump_decks(self, decks):
        with open(DECKS_PICKLE, "wb") as file:
            pickler = pickle.Pickler(file)

            pickler.dump(decks)

    def total(self):
        total_with = 0
        total_without = 0

        for j_type in JOKERS_VALUES:

            temp_nbr = int(self.temp[j_type])
            joker_nbr = int(self.jokers[j_type])
            res_with = temp_nbr - joker_nbr

            if res_with < 0:
                res_with = 0

            total_with += res_with * JOKERS_VALUES[j_type]
            total_without += temp_nbr * JOKERS_VALUES[j_type]

        total_with = str(total_with)
        total_without = str(total_without)

        self.temp['total_with'] = total_with
        self.temp['total_without'] = total_without


    def add_deck(self):
        print("Add a new deck :\n")

        deck = {
            "name"          : None,
            "champions"     : None,
            "purples"       : None,
            "blues"         : None,
            "greens"        : None,
            "total_without" : None,
            "total_with"    : None
        }

        for value in deck:
            deck[value] = input("{} :".format(value))
            if value == 'greens':
                break

        self.temp = deck

        self.total()

        decks = self.get_decks()
        decks.append(self.temp)
        self.dump_decks(decks)

        print(deck['name'] + " added.")

    def delete_deck(self):
        print("Delete an existent deck :")

        decks = self.get_decks()

        i = 1
        for deck in decks:
            print("{}. {}, cost: {}".format(i, deck['name'], deck['total_without']))
            i += 1

        res = input("enter the id of the deck you want to delete :")
        res = int(res) - 1

        name = decks[res]['name']
        del decks[res]

        self.dump_decks(decks)

        print(name + " properly removed.")

    def update_decks(self):
        decks = self.get_decks()

        for deck in decks:
            self.temp = deck
            self.total()
            deck = self.temp

        self.dump_decks(decks)