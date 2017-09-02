''' Contains the PlayerManager class, which keeps track of all Players and adjusts
    their attributes as needed'''
from Player_class import Player
from PlayerFactory import *

class PlayerManager:
    '''Maintains a collection of all player instances'''
    def __init__(self):
        self.all_players = {}

    def load_players(self, NBA_teams, NBA_teams_checklist):
        '''call PlayerFactory to load all players from the database'''
        players = PlayerFactory.players_from_db(NBA_teams)
        for player in players:
            #UNCOMMENT THE NEXT LINE TO TEST WIN SHARES
            #PlayerFactory.win_shares(player, NBA_teams, NBA_teams_checklist)
            self.all_players[player.get_player_id()] = player

    def get_player_with_id(self, id):
        '''return a specifc player'''
        return self.all_players[id]
