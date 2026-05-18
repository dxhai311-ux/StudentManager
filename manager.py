from storage import load_students, save_students
from student import Student

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

def get_avg(students):
	if not students:
		print('No students')
		return

	res = sum(score for name, score in students.items()) / len(students)
	print(f"Average score : {res:.2f}")

def get_top(students):
	if not students:
		print('No students')
		return

	top_name, top_score = max(students.items(), key = lambda x : x[1])
	print(f"Top student : {top_name} - {top_score}")

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

def sort_student(students):
	if not students:
		print('No students')
		return

	print('\nDANH SACH SAP XEP :')
	sort_list = sorted(students.items(), key = lambda x : x[1], reverse = True)
	for name, score in sort_list:
		print(f"{name} - {score}")

def filter_score(students):
	if not students:
		print('No students')
		return

	for ten, score in students.items():
		sv = Student(ten, score)
		print(f"{sv.ten} - {sv.score} - {sv.filter_by_score()}")