import json
from student import Student
from storage import save_students, load_students
from manager import (
    show_students,
    add_student,
    delete_student,
    update_student,
    search_student,
    get_avg,
    get_top,
    sort_student, 
    filter_score
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
		print('8. Sort student')
		print('9. Filter by score')
		print('10. Exit')
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
			get_avg(students)
		elif select == 4:
			get_top(students)
		elif select == 5:
			delete_student(students)
		elif select == 6:
			update_student(students)
		elif select == 7:
			search_student(students)
		elif select == 8:
			sort_student(students)
		elif select == 9:
			filter_score(students)
		elif select == 10:
			check = False
		else:
			print('Invalid select')