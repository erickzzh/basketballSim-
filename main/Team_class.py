from Player_class import *

class Team:
	'''allows for easier interaction with data in the teams table'''
	def __init__(self, team_name_abbr, team_name):
		self.teamid = 0
		self.team_name_abbr = team_name_abbr
		self.team_name = team_name
		#if this is decleared outside then the roster list is shared with the other instances in this case it is not
		self.roster = []
		self.roster_class = {}
		self.expected_winning_percentage = {}
		self.offensive_efficiency = 0
		self.defensive_efficiency = 0
		self.positions_per_game = 0
		self.effective_field_goal_percentage = 0
		self.turnover_rate = 0
		self.offensive_rebounding_percentage = 0
		self.free_throw_rate = 0
		self.winning_percentage = 0
		self.game_schedule = []
		self.sim_win = 0
		self.sim_FAT_L = 0
		self.possessions = 0
		self.points_allowed = 0
		self.free_throw_attempts = 0
		self.field_goal_attempts = 0
		self.turnover = 0
		self.offensive_rebounds = 0
		self.points_scored = 0
		self.treys_made = 0
		self.free_throw_made = 0

		self.field_goal_attempts_pct = 0
		self.defensive_rebonds = 0
		self.opponent_fg_pct = 0
		self.opponent_dor_pct = 0
		self.opponent_possession = 0

	@classmethod
	def alt_init(cls, team_name_abbre, team_name):
		return cls(team_name_abbre, team_name)





	def change_effeiciency(self):
		self.offensive_efficiency = 99999
	#first create a complete roster in the list roster[]
	def add_players_roster(self, players):
		self.roster.insert(len(self.roster), players)

	def add_player(self, player):
		self.roster_class[player.get_full_name()] = player
		# print("%s, PPG: %.2f, Effective FG%%: %.2f" % (self.roster_class[player.get_full_name()].get_full_name(),
		# 						self.roster_class[player.get_full_name()].get_points(),
		# 						self.roster_class[player.get_full_name()].get_effective_field_goal_percentage()))

	def trade_players_roster(self, leaving_player, coming_player):
		self.roster = [player.replace(leaving_player, coming_player) for player in self.roster]

#printer
	def print_roster(self):
		print (self.roster)

	def print_roster_and_points(self):
		for i in self.roster_class:
			print (i, self.roster_class[i].points_per_game)

	def print_team_name_abbr(self):
		print (self.team_name_abbr)

	def print_team_name(self):
		print (self.team_name)

	def print_player_points_helper(self, player_name):
		self.roster_class[player_name].print_points_per_game()

	def print_team_theoretical_points(self):
		team_total_points = 0.0
		for x in self.roster:
			team_total_points = team_total_points + self.roster_class[x].get_points()

		print ("%0.2f" % team_total_points)

		return team_total_points

	def print_team_winning_percentage(self):
		print (self.winning_percentage)



#getter 
	def get_team_theoretical_points(self):
		'''calculates the team theoretical points if everyone plays'''
		team_total_points = 0.0
		for x in self.roster:
			team_total_points = team_total_points+self.roster_class[x].get_points()
			team_total_points = round(team_total_points,2)
		return team_total_points

	def get_sim_win(self):
		return self.sim_win

	def get_sim_FAT_L(self):
		return self.sim_FAT_L

	def change_effeiciency(self):
		self.offensive_efficiency = 99999

	def get_possessions(self):
		return self.possessions

	def get_points_allowed(self):
		return self.points_allowed

	def get_free_throw_attempts(self):
		return self.free_throw_attempts

	def get_field_goal_attempts(self):
		return self.field_goal_attempts

	def get_turnover(self):
		return self.turnover

	def get_opponent_possession(self):
		return self.opponent_possession

#setter
	def set_teamID(self,value):
		self.teamid = value
	
	def set_team_name_abbr(self,value):
		self.team_name_abbr = value

	def set_team_name(self,value):
		self.team_name = value
		
	def set_offensive_efficiency(self,value):
		self.offensive_efficiency = value

	def set_defensive_efficiency(self,value):
		self.defensive_efficiency = value

	def set_possessions_per_game(self,value):
		self.positions_per_game = value

	def set_effective_field_goal_percentage(self,value):
		self.effective_field_goal_percentage = value

	def set_turnover_rate(self,value):
		self.turnover_rate = value

	def set_offensive_rebounding_percentage(self,value):
		self.offensive_rebounding_percentage = value

	def set_free_throw_rate(self,value):
		self.free_throw_rate = value

	def set_winning_percentage(self,value):
		self.winning_percentage = value

	def set_sim_win(self,value):
		self.sim_win = value

	def set_sim_FAT_L(self,value):
		self.sim_FAT_L = value

	def set_field_goal_attempts(self,value):
		self.field_goal_attempts = value

	def set_free_throw_attempts(self,value):
		self.free_throw_attempts = value

	def set_turnover(self,value):
		self.turnover = value

	def set_possessions(self, value):
		self.possessions = value

	def set_points_allowed(self, value):
		self.points_allowed = value

	def set_offensive_rebounds(self,value):
		self.offensive_rebounds = value

	def set_points_scored(self,value):
		self.points_scored = value

	def set_treys_made(self,value):
		self.treys_made = value

	def set_field_goal_attempts_pct(self,value):
		self.field_goal_attempts_pct = value

	def set_defensive_rebonds(self,value):
		self.defensive_rebonds = value

	def set_opponent_fg_pct(self,value):
		self.opponent_fg_pct = value

	def set_opponent_dor_pct(self,value):
		self.opponent_dor_pct = value

	def set_opponent_possession(self,value):
		self.opponent_possession = value

	def set_team_name(self,value):
		self.team_name = value

	def set_free_throw_made(self,value):
		self.free_throw_made = value