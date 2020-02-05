import random
import math
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

class Model:

    def __init__(self, players=4, simulations=1000, game="Spoons", ranking=False):
        self.players = players
        self.simulations = simulations
        self.game = game
        self.ranking = ranking
    
    def run(self):
        pass

class SpoonSimulation:

    def __init__(self, ranking=False):
        self.ranking = ranking
    
class Deck:

    def __init__(self):
        pass


try:
    test = open("TestingFile.txt", 'w')
except:
    print("no good")


        