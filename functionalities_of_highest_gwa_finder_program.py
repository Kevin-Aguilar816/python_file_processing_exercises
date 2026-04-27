class Student:
    def __init__(self, name, gwa):
        self.name = name.strip()
        self.gwa = float(gwa)

    def __str__(self):
        return f"{self.name} - GWA: {self.gwa:.2f}"

    def __repr__(self):
        return f"Student(name='{self.name}', gwa={self.gwa})"


class StudentRecordProcessor:
    def __init__(self, input_filename="students.txt"):
        self.input_filename = input_filename
        self.students = []
        self.top_student = None
