class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def average(self):
        if not self.marks:
            return 0
        return sum(self.marks) / len(self.marks)


class Classroom:
    def __init__(self):
        self.students = {}

    def add_student(self, student):
        self.students[student.name] = student.average()

    def average_marks(self):
        return self.students

    def top_performer(self):
        if not self.students:
            return None
        return max(self.students, key=self.students.get)


students_data = {"John": [85, 78, 92], "Alice": [88, 79, 95], "Bob": [70, 75, 80]}
classroom = Classroom()

for name, marks in students_data.items():
    classroom.add_student(Student(name, marks))

print("Average Marks:", classroom.average_marks())
top_student = classroom.top_performer()
if top_student:
    print("Top Performer:", top_student)
else:
    print("No student data available.")
