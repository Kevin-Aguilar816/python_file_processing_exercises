from functionalities_of_highest_gwa_finder_program import Student, StudentRecordProcessor
uploaded_files = ["students.txt"]


def main():
    processor = StudentRecordProcessor()
    if not processor.read_student_record_from_file():
        return

    processor.find_highest_gwa()
    processor.display_highest_gwa()


if __name__ == "__main__":
    main()
