from Player_class import * 

class Team:
	def __init__(self,team_name_abbr,team_name):
		self.team_name_abbr=team_name_abbr
		self.team_name=team_name
		#if this is decleared outside then the roster list is shared with the other instances in this case it is not
		self.roster=[]
		self.roster_class={}
		self.offensive_efficiency=0
		self.defensive_efficiency=0
		self.positions_per_game=0




	def print_roster(self):
		print (self.roster)

	def print_roster_and_points(self):
		for i in self.roster_class:
			print (i,self.roster_class[i].points_per_game)

	def print_team_name_abbr(self):
		print (self.team_name_abbr)
	def print_team_name(self):
		print (self.team_name)



#first create a complete roster in the list roster[]
	def add_players_roster(self,players):
		self.roster.insert(len(self.roster),players)
#second create a dictionary and create a class for each element of the player then its fking go time
	def add_players_class(self,first_name,last_name,points_per_game,position):
		self.roster_class[first_name+last_name]=Player(first_name,last_name,position,points_per_game)
		

	def print_player_points_helper(self,player_name):
		self.roster_class[player_name].print_points_per_game()

	def trade_players_roster(self,leaving_player,coming_player):
		self.roster=[player.replace(leaving_player,coming_player) for player in self.roster]




#calculates the team theoretical points if everyone plays
	def print_team_theoretical_points(self):
		team_total_points=0.0
		for x in self.roster:
			team_total_points=team_total_points+self.roster_class[x].get_points()
		print("%0.2f" % team_total_points)
		return team_total_points

	def get_team_theoretical_points(self):
		team_total_points=0.0
		for x in self.roster:
			team_total_points=team_total_points+self.roster_class[x].get_points()
			team_total_points=round(team_total_points,2)
		return team_total_points

	def change_effeiciency(self):
		self.offensive_efficiency=99999


