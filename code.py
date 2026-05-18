import json
from student import Student
from storage import save_students, load_students
from manager import (
    show_students,
    add_student,
    delete_student,
    update_student,
    search_student
)

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