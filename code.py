import json

class Student:
	def __init__(self, ten, score):
		self.ten = ten
		self.score = score

	def __str__(self):
		return f"{self.ten} {self.score}"

def save_students(students):
	with open('students.json', 'w') as file:
		json.dump(students, file, indent = 4)

def load_students():
	try:
		with open('students.json', 'r') as file:
			return json.load(file)
	except FileNotFoundError:
		return {}

def show_students(students):
	for name, score in students.items():
		sv = Student(name, score)
		print(sv)

def add_student(students):
	name = input('Enter name :').title()
	if name not in students:
		try:
			score = float(input('Enter score :'))
			if 0 <= score <= 10:
				students[name] = score
				save_students(students)
			else:
				print('Score Invalid')
		except ValueError:
				print('Invalid score')	
	else:
		print('Student already exists')

def delete_student(students):
	name_del = input('Enter name to delete :').title()
	if name_del in students:
		del students[name_del]
		save_students(students)
		print('Delete succesfully')
	else:
		print('Invalid name')

def update_student(students):
	name_update = input('Enter student name :').title()
	if name_update not in students:
		print('Invalid name')
		return 
	try:
		score_update = float(input('Enter new score :'))
		if 0 <= score_update <= 10:	
			students[name_update] = score_update
			save_students(students)
			print('Update succesfully')
		else:
			print('Invalid score')
	except ValueError:
		print('Invalid score update')

def search_student(students):
	name_search = input('Enter name search :').title()
	if name_search in students:
		print(name_search, students[name_search], sep = ' - ')
	else:
		print('Student not found')

if __name__ == '__main__':
	students = load_students()
	check = True
	while check:
		print('\n===== Student Manager =====')
		print('1. Show students')
		print('2. Add student')
		print('3. Average score calculation')
		print('4. Top student')
		print('5. Delete student')
		print('6. Update score')
		print('7. Search student')
		print('8. Exit')
		try:
			select = int(input('Enter choice : '))
		except ValueError:
			print('Invalid input')
			continue
		if select == 1:
			show_students(students)
		elif select == 2:
			add_student(students)
		elif select == 3:
			if not students:
				print('No students')
				continue

			res = sum(score for name, score in students.items()) / len(students)
			print(f"Average score : {res:.2f}")
		elif select == 4:
			if not students:
				print('No student')
				continue

			top_name, top_score = max(students.items(), key = lambda x : x[1])
			print(f"Top student : {top_name} - {top_score}")
		elif select == 5:
			delete_student(students)
		elif select == 6:
			update_student(students)
		elif select == 7:
			search_student(students)
		elif select == 8:
			check = False
		else:
			print('Invalid select')