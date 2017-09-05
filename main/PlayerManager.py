''' Contains the PlayerManager class, which keeps track of all Players and adjusts
    their attributes as needed'''
from Player_class import Player
from PlayerFactory import *
from collections import OrderedDict
class PlayerManager:
    '''Maintains a collection of all player instances'''
    def __init__(self):
        self.all_players = {}

    def load_players(self, NBA_teams, NBA_teams_checklist):
        '''call PlayerFactory to load all players from the database'''
        players = PlayerFactory.players_from_db(NBA_teams)
        for player in players:
            #UNCOMMENT THE NEXT LINE TO TEST WIN SHARES
            PlayerFactory.win_shares(player, NBA_teams, NBA_teams_checklist)
            self.all_players[player.get_player_id()] = player

    def get_player_with_id(self, id):
        '''return a specifc player'''
        return self.all_players[id]

    def rank_by_win_shares(self):
        '''print all players, ranked in desc. order by win share total'''
        temp_players = {}
        for key, value in self.all_players.items():
            temp_players[self.all_players[key].get_full_name()] = self.all_players[key].get_total_win_share()
        
        ranked = OrderedDict(sorted(temp_players.items(), key = lambda t: t[1], reverse= True))
        for key, value in ranked.items():
            print("%s total win share: %.2f" % (key, value))
