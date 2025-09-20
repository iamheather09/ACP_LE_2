class student:
    def __init__(self, student_id, student_name, email, grades=None, courses=None):
# 👉 initialize attributes here
        self.student_id = student_id
        self.student_name = student_name
        self.email = email
        self.grades = grades if grades is not None else{}
        self.courses = courses if courses is not None else{}     
        pass 
     
    def __str__(self):
        return f"Student ID: {self.student_id}, Name: {self.student_name}, Email: {self.email}, Grades: {self.grades}, Courses: {self.courses}"
    
    
