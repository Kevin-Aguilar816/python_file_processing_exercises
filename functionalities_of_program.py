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
