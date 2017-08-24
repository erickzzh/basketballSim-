class Player:
	def __init__(self,FirstName,LastName,Position,points_per_game):
		self.FirstName=FirstName
		self.LastName=LastName
		self.FullName=FirstName + LastName
		self.Position=Position
		self.points_per_game=points_per_game
		self.effective_field_goal_percentage = 0
		self.true_shooting_percentage = 0
		self.field_goal_attempts = 0
		self.field_goals_made = 0
		self.free_throw_attempts = 0
		self.treys_made = 0
	def print_name(self):
		print (self.FullName)

	def print_points_per_game(self):
		print (self.points_per_game)

	def print_position(self):
		print(self.Position)

	#getters
	def get_points(self):
		return self.points_per_game
	
	def get_full_name(self):
		return self.FullName

	def get_field_goal_attempts(self):
		return self.field_goal_attempts

	def get_field_goals_made(self):
		return self.field_goals_made

	def get_free_throw_attempts(self):
		return self.free_throw_attempts

	def get_treys_made(self):
		return self.treys_made

	def get_effective_field_goal_percentage(self):
		return self.effective_field_goal_percentage

	def get_true_shooting_percentage(self):
		return self.true_shooting_percentage

	#setters
	def set_true_shooting_percentage(self, value):
		self.true_shooting_percentage = value
	
	def set_effective_field_goal_percentage(self, value):
		self.effective_field_goal_percentage = value

	def set_field_goal_attempts(self,value):
		self.field_goal_attempts = value
	
	def set_field_goals_made(self,value):
		self.field_goals_made = value

	def set_free_throw_attempts(self,value):
		self.free_throw_attempts = value
	
	def set_treys_made(self, value):
		self.treys_made = value
	
	def set_points_per_game(self, value):
		self.points_per_game = value
	
	@classmethod
	def alt_init(cls, FirstName, LastName, Position):
		return cls(FirstName,LastName,Position,0)
