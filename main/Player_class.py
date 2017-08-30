class Player:
	'''Instances of this class hold data from the players table for easier interaction'''
	def __init__(self, FirstName, LastName, Position, points_per_game):
		self.player_id = 0
		self.team_id = 0
		self.FirstName = FirstName
		self.LastName = LastName
		self.FullName = FirstName + " " + LastName
		self.Position = Position
		self.points_per_game = points_per_game
		self.assists_per_game = 0
		self.effective_field_goal_percentage = 0
		self.true_shooting_percentage = 0
		self.field_goal_attempts = 0
		self.field_goals_made = 0
		self.free_throw_attempts = 0
		self.free_throws_made = 0
		self.treys_made = 0
		self.off_reb_per_game = 0
		self.points_produced = 0
		self.player_usage = 0
		self.turnover = 0
		self.minutes = 0

	def print_name(self):
		print (self.FullName)

	def print_points_per_game(self):
		print (self.points_per_game)

	def print_position(self):
		print (self.Position)

	#getters
	def get_player_id(self):
		return self.player_id

	def get_team_id(self):
		return self.team_id

	def get_points(self):
		return self.points_per_game

	def get_assists_per_game(self):
		return self.assists_per_game

	def get_full_name(self):
		return self.FullName

	def get_field_goal_attempts(self):
		return self.field_goal_attempts

	def get_field_goals_made(self):
		return self.field_goals_made

	def get_free_throw_attempts(self):
		return self.free_throw_attempts

	def get_free_throws_made(self):
		return self.free_throws_made

	def get_treys_made(self):
		return self.treys_made

	def get_effective_field_goal_percentage(self):
		return self.effective_field_goal_percentage

	def get_true_shooting_percentage(self):
		return self.true_shooting_percentage

	def get_off_reb_per_game(self):
		return self.off_reb_per_game

	def get_points_produced(self):
		return self.points_produced

	def get_player_usage(self):
		return self.player_usage

	def get_player_turnover(self):
		return self.turnover

	def get_player_minutes(self):
		return self.minutes

	#setters
	def set_player_id(self, value):
		self.player_id = value

	def set_team_id(self, value):
		self.team_id = value

	def set_true_shooting_percentage(self, value):
		self.true_shooting_percentage = value

	def set_effective_field_goal_percentage(self, value):
		self.effective_field_goal_percentage = value

	def set_field_goal_attempts(self, value):
		self.field_goal_attempts = value

	def set_field_goals_made(self, value):
		self.field_goals_made = value

	def set_free_throw_attempts(self, value):
		self.free_throw_attempts = value

	def set_free_throws_made(self, value):
		self.free_throws_made = value

	def set_treys_made(self, value):
		self.treys_made = value

	def set_points_per_game(self, value):
		self.points_per_game = value

	def set_assists_per_game(self, value):
		self.assists_per_game = value

	def set_off_reb_per_game(self, value):
		self.off_reb_per_game = value

	def set_points_produced(self, value):
		self.points_produced = value

	def set_player_usage(self,value):
		self.player_usage = value

	def set_turnover(self,value):
		self.turnover = value

	def set_minutes(self,value):
		self.minutes = value
	@classmethod
	def alt_init(cls, FirstName, LastName, Position):
		return cls(FirstName, LastName, Position, 0)
