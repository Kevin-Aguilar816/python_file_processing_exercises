from functionalities_of_program import NumberProcessor
uploaded_file = "numbers.txt"


def main():
    processor = NumberProcessor()

    if processor.read_numbers_from_file():
        if processor.classify_numbers():
            processor.write_even_numbers_to_file()
            processor.write_odd_numbers_to_file()


if __name__ == "__main__":
    main()
