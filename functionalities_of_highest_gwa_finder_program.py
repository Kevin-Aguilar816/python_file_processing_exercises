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
            with open(self.input_filename, 'r', encoding='utf-8') as file:
                lines = file.readlines()

            self.students = []
            for line_num, line in enumerate(lines, 1):
                line = line.strip()
                if not line:
                    continue

                try:
                    parts = line.split()
                    if len(parts) < 2:
                        print(
                            f"Warning: Line {line_num} invalid format: '{line}'. Skipping.")
                        continue

                    name = " ".join(parts[:-1])
                    gwa = parts[-1].strip()
                    student = Student(name, gwa)
                    self.students.append(student)

                except ValueError as ve:
                    print(
                        f"Warning: Line {line_num} invalid GWA '{line}': {ve}. Skipping.")
                    continue

            print(
                f"Successfully read {len(self.students)} student records from '{self.input_filename}'")
            return True

        except FileNotFoundError:
            print(f"Error: File '{self.input_filename}' not found!")
            return False
        except PermissionError:
            print(f"Error: Permission denied for '{self.input_filename}'")
            return False
        except Exception as e:
            print(f"Unexpected error reading '{self.input_filename}': {e}")
            return False

    def find_highest_gwa(self):
        if not self.students:
            print("No valid student records to process.")
            return False

        self.top_student = max(self.students, key=lambda student: student.gwa)
        print(f"found top student: {self.top_student}")
        return True

    def display_highest_gwa(self):
        if self.top_student:
            print(
                f"The student with the highest GWA is: {self.top_student.name} with a GWA of {self.top_student.gwa:.2f}")
        else:
            print("No top student found. Please ensure records are processed.")
