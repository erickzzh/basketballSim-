class Player:
	def __init__(self,FirstName,LastName,Position,points_per_game):
		self.FirstName=FirstName
		self.LastName=LastName
		self.FullName=FirstName + LastName
		self.Position=Position
		self.points_per_game=points_per_game
		self.effective_field_goal_percentage = 0
		self.true_shooting_percentage = 0
	def print_name(self):
		print (self.FullName)

	def print_points_per_game(self):
		print (self.points_per_game)

	def print_position(self):
		print(self.Position)

	def get_points(self):
		return self.points_per_game
	
	def get_full_name(self):
		return self.FullName

	def set_true_shooting_percentage(self, value):
		self.true_shooting_percentage = value
	
	def set_effective_field_goal_percentage(self, value):
		self.effective_field_goal_percentage = value

	@classmethod
	def alt_init(cls, FirstName, LastName, Position):
		return cls(FirstName,LastName,Position,0)
