class Student:
	def __init__(self, ten, score):
		self.ten = ten
		self.score = score

	def filter_by_score(self):
		if self.score >= 5:
			return 'DO'
		else:
			return 'TRUOT'

	def __str__(self):
		return f"{self.ten} {self.score}"