class NumberProcessor:
    def __init__(self, input_filename="numbers.txt"):
        self.input_filename = input_filename
        self.numbers = []
        self.even_numbers = []
        self.odd_numbers = []

    def read_numbers_from_file(self):
        try:
            with open(self.input_filename, 'r') as file:
                self.numbers = [int(line.strip()) for line in file.readlines()]
            print(
                f"Successfully read {len(self.numbers)} numbers from {self.input_filename}")
            return True
        except FileNotFoundError:
            print(f"Error: The file {self.input_filename} was not found.")
            return False
        except ValueError:
            print(
                f"Error: The file {self.input_filename} contains non-integer values.")
            return False
        except Exception as error:
            print(f"An unexpected error occurred: {error}")
            return False

    def classify_numbers(self):
        if not self.numbers:
            print("No numbers to classify. Please read numbers from the file first.")
            return False

        self.even_numbers = [num for num in self.numbers if num % 2 == 0]
        self.odd_numbers = [num for num in self.numbers if num % 2 != 0]

        print(
            f"Classified {len(self.even_numbers)} even numbers and {len(self.odd_numbers)} odd numbers.")
        return True

    def write_even_numbers_to_file(self, output_filename="even.txt"):
        if not self.even_numbers:
            print("No even numbers to write. Please classify numbers first.")
            return False

        try:
            with open(output_filename, 'w') as file:
                for num in self.even_numbers:
                    file.write(f"{num}\n")
            print(
                f"Successfully wrote {len(self.even_numbers)} even numbers to {output_filename}")
            return True
        except Exception as error:
            print(f"An error occurred while writing to the file: {error}")
            return False

    def write_odd_numbers_to_file(self, output_filename="odd.txt"):
        if not self.odd_numbers:
            print("No odd numbers to write. Please classify numbers first.")
            return False

        try:
            with open(output_filename, 'w') as file:
                for num in self.odd_numbers:
                    file.write(f"{num}\n")
            print(
                f"Successfully wrote {len(self.odd_numbers)} odd numbers to {output_filename}")
            return True
        except Exception as error:
            print(f"An error occurred while writing to the file: {error}")
            return False

    def process_numbers(self):
        if not self.read_numbers_from_file():
            return False

        if not self.classify_numbers():
            return False
        even_numbers_read = self.write_even_numbers_to_file()
        odd_numbers_read = self.write_odd_numbers_to_file()
        return even_numbers_read and odd_numbers_read
