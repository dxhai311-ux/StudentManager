class Student:
	def __init__(self, ten, score):
		self.ten = ten
		self.score = score

	def __str__(self):
		return f"{self.ten} {self.score}"