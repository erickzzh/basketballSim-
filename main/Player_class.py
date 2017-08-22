class Player:
	def __init__(self,FirstName,LastName,Position,points_per_game):
		self.FirstName=FirstName
		self.LastName=LastName
		self.FullName=FirstName + LastName
		self.Position=Position
		self.points_per_game=points_per_game
	def print_name(self):
		print (self.FullName)

	def print_points_per_game(self):
		print (self.points_per_game)

	def print_position(self):
		print(self.Position)

	def get_points(self):
		return self.points_per_game


