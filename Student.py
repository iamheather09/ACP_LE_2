class Student:
    def __init__(self, student_id, student_name, email, grades=None, courses=None):
        self.id_name = (student_id, student_name)
        self.email = email
        self.grades = grades if grades else {}
        self.courses = courses if courses else set()

    def __str__(self):
        return (
            f"ID: {self.id_name[0]}, Name: {self.id_name[1]}, Email: {self.email},\n"
            f"Courses: {', '.join(self.courses) if self.courses else 'None'},\n"
            f"Grades: {self.grades if self.grades else 'No grades recorded'}"
        )

class StudentRecords:
    def __init__(self):
        self.students = []

    def add_student(self, student_id, student_name, email, grades=None, courses=None):
        if any(s.id_name[0] == student_id for s in self.students):
            return "Student with this ID already exists."
        student = Student(student_id, student_name, email, grades, courses)
        self.students.append(student)
        return "Student added successfully."

    def update_student(self, student_id, email=None, grades=None, courses=None):
        for student in self.students:
            if student.id_name[0] == student_id:
                if email:
                    student.email = email
                if grades:
                    student.grades.update(grades)
                if courses:
                    student.courses.update(courses)
                return "Student updated successfully."
        return "Student not found."

    def delete_student(self, student_id):
        for i, student in enumerate(self.students):
            if student.id_name[0] == student_id:
                del self.students[i]
                return "Student deleted successfully."
        return "Student not found."

    def enroll_course(self, student_id, course):
        for student in self.students:
            if student.id_name[0] == student_id:
                student.courses.add(course)
                return f"Student enrolled in {course}."
        return "Student not found."

    def search_student(self, student_id):
        for student in self.students:
            if student.id_name[0] == student_id:
                return str(student)
        return "Student not found."

# Example usage:

# Initialize the student records manager
records = StudentRecords()

# Add some students
print(records.add_student(101, "Allen Paloma", "allenpaloma@gmail.com"))
print(records.add_student(102, "Heather Lourd", "heatherlourd@gmail.com"))

# Update a student's email and grades
print(records.update_student(101, email="heatherlourd@gmail.com", grades={"Math": 90, "Science": 85}))

# Enroll in a new course
print(records.enroll_course(101, "Astronomy"))

# Search for a student
print(records.search_student(101))

# Delete a student
print(records.delete_student(102))

