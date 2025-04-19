# src/record_manager.py

from student import Student

class StudentRecordManager:
    """Handles all student record operations."""
    
    def __init__(self):
        self.records = []

    def add_student(self, name, student_id):
        student = Student(name, student_id)
        self.records.append(student)

    def remove_student(self, student_id):
        self.records = [s for s in self.records if s.student_id != student_id]

    def list_students(self):
        return [str(s) for s in self.records]
