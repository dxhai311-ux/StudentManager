
class Student:
	def __init__(self, ten, score):
		self.ten = ten
		self.score = score



	def __str__(self):
		return f"{self.ten} {self.score}"


if __name__ == '__main__':
	students = {
		'Hai' : 8.5,
		'Huong' : 9.2,
		'Thu' : 7.0
	}
	check = True
	while check:
		print('\n===== Student Manager =====')
		print('1. Show students')
		print('2. Add student')
		print('3. Average score calculation')
		print('4. Top student')
		print('5. Delete student')
		print('6. Update score')
		print('7. Exit')
		select = int(input('Enter choice : '))
		if select == 1:
			for name, score in students.items():
				sv = Student(name, score)
				print(sv)
		elif select == 2:
			name = input('Enter name :')
			try:
				score = float(input('Enter score :'))
				students[name] = score
			except ValueError:
				print('Invalid score')	
		elif select == 3:
			res = sum(score for name, score in students.items()) / len(students)
			print(f"Average score : {res:.2f}")
		elif select == 4:
			top_name, top_score = max(students.items(), key = lambda x : x[1])
			print(f"Top student : {top_name} - {top_score}")
		elif select == 5:
			name_del = input('Enter name to delete :')
			found = False
			for name in list(students.keys()):
				if name.title() == name_del.title():
					students.pop(name)
					found = True
					print('Delete succesfully')
					break
			if not found:
				print('Invalid name')
		elif select == 6:
			name_update = input('Enter student name :')
			score_update = float(input('Enter new score :'))
			check = False
			for name, score in students.items():
				if name == name_update:
					check = True
					students[name] = score_update
					break
			if not check:
				print('Invalid name')
		elif select == 7:
			check = False
		else:
			print('Invalid select')