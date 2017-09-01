''' Contains the PlayerManager class, which keeps track of all Players and adjusts
    their attributes as needed'''
from Player_class import Player
from PlayerFactory import *

class PlayerManager:
    '''Maintains a collection of all player instances'''
    def __init__(self):
        self.all_players = []

    def load_players(self):
        '''call PlayerFactory to load all players from the database'''
        self.all_players = PlayerFactory.players_from_db()
