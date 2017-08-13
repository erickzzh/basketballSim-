class Team:
	team_name="DEFAULT"
	

	def __init__(self,team_name):
		self.team_name=team_name
		#if this is decleared outside then the roster list is shared with the other instances in this case it is not
		self.roster=[]
	def print_roster(self):
		print (self.roster)

	def print_team_name(self):
		print (self.team_name)

	def add_players(self,players):
		self.roster.insert(len(self.roster),players)

