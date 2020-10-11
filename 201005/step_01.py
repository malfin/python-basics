import students_stat

students_log = students_stat.parse_marks('students_log.txt')
students_log_as_dict = students_stat.parse_marks_as_dict('students_log.txt')
# students_stat.show_students(students_log)
# students_stat.show_students_dict(students_log_as_dict)
# students_stat.show_marks(students_log, raw=True)
# students_stat.show_marks(students_log, raw=False)
# students_stat.show_marks(students_log, raw=False, sep=' | ')
students_stat.save_marks('students_log.csv', students_log)
students_stat.save_marks_as_dict('students_log.json', students_log_as_dict)