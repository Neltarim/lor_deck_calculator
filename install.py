from os import mkdir
import pickle

from core.const import JOKERS_PICKLE, DECKS_PICKLE
from ldc import main


mkdir(DATA_PATH)

deck = {
            "name"          : "Template, delete me",
            "champions"     : 0,
            "purples"       : 0,
            "blues"         : 0,
            "greens"        : 0,
            "total_without" : 0,
            "total_with"    : 0
        }

decks = []
decks.append(deck)

with open(DECKS_PICKLE, "wb") as file:
    pickler = pickle.Pickler(file)

    pickler.dump(decks)

jokers = {
    "champions" : 0,
    "purples" : 0,
    "blues" : 0,
    "greens" : 0
}

with open(JOKERS_PICKLE, "wb") as file:
    pickler = pickle.Pickler(file)

    pickler.dump(jokers)