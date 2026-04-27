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

    def read_student_record_from_file(self):
        try:
            with open(self.input_filename, 'r') as file:
                lines = file.readlines()

            self.students = []
            for line_num, line in enumerate(lines, start=1):
                line = line.strip()
                if not line:
                    continue
