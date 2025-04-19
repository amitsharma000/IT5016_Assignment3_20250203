# src/student.py

class Student:
    """Represents a student with name and student ID."""
    
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id

    def __str__(self):
        return f"Student(Name: {self.name}, ID: {self.student_id})"
