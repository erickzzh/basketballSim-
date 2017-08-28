from Player_class import * 

class Team:
	def __init__(self,team_name_abbr,team_name):
		self.teamid=0
		self.team_name_abbr=team_name_abbr
		self.team_name=team_name
		#if this is decleared outside then the roster list is shared with the other instances in this case it is not
		self.roster=[]
		self.roster_class={}
		self.expected_winning_percentage={}
		self.offensive_efficiency=0
		self.defensive_efficiency=0
		self.positions_per_game=0
		self.effective_field_goal_percentage = 0
		self.turnover_rate = 0
		self.offensive_rebounding_percentage = 0
		self.free_throw_rate = 0
		self.winning_percentage=0


#printer
	def print_roster(self):
		print (self.roster)

	def print_roster_and_points(self):
		for i in self.roster_class:
			print (i,self.roster_class[i].points_per_game)

	def print_team_name_abbr(self):
		print (self.team_name_abbr)
	def print_team_name(self):
		print (self.team_name)
	def print_player_points_helper(self,player_name):
		self.roster_class[player_name].print_points_per_game()
	def print_team_theoretical_points(self):
		team_total_points=0.0
		for x in self.roster:
			team_total_points=team_total_points+self.roster_class[x].get_points()
		print("%0.2f" % team_total_points)
		return team_total_points
	def print_team_winning_percentage(self):
		print(self.winning_percentage)

#first create a complete roster in the list roster[]
	def add_players_roster(self,players):
		self.roster.insert(len(self.roster),players)

	def add_player(self, player):
		self.roster_class[player.get_full_name()] = player
		print("%s, PPG: %.2f, Effective FG%%: %.2f" % (self.roster_class[player.get_full_name()].get_full_name(), 
								self.roster_class[player.get_full_name()].get_points(),
								self.roster_class[player.get_full_name()].get_effective_field_goal_percentage()))

	

	def trade_players_roster(self,leaving_player,coming_player):
		self.roster=[player.replace(leaving_player,coming_player) for player in self.roster]




#calculates the team theoretical points if everyone plays


	def get_team_theoretical_points(self):
		team_total_points=0.0
		for x in self.roster:
			team_total_points=team_total_points+self.roster_class[x].get_points()
			team_total_points=round(team_total_points,2)
		return team_total_points

	def change_effeiciency(self):
		self.offensive_efficiency=99999


