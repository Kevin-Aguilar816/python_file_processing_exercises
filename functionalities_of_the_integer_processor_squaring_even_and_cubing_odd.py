class IntegerProcessor:
    def __init__(self, source_file="integers.txt"):
        self.source_file = source_file
        self.integers = []
        self.even_integrs = []
        self.odd_integers = []
        self.even_squared = []
        self.odd_cubed = []

    def read_integers(self):
        try:
            with open(self.source_file, 'r') as file:
                lines = [line.strip() for line in file.readlines()]

                self.integers = []
                for i, line in enumerate(lines, 1):
                    if not line:
                        continue
                    try:
                        num = int(line)
                        self.integers.append(num)
                    except ValueError:
                        print(
                            f"Warning: Line {i + 1} in '{self.source_file}' is not a valid integer and will be skipped.")
                print(
                    f"Rad {len(self.integers)} integers from '{self.source_file}'.")
                if len(self.integers) != 20:
                    print(f"Expected 20 integers, found {len(self.integers)}")
                return True

        except FileNotFoundError:
            print(f"Error: The file '{self.source_file}' was not found.")
            return False
        except Exception as error:
            print(f"An error occurred while reading the file: {error}")
            return False

    def classify_and_transform(self):
        if not self.integers:
            print("No integers to process. Please read integers first.")
            return False

        self.even_integers = [num for num in self.integers if num % 2 == 0]
        self.odd_integers = [num for num in self.integers if num % 2 != 0]

        self.even_squared = [num ** 2 for num in self.even_integers]
        self.odd_cubed = [num ** 3 for num in self.odd_integers]

        return True

    def write_double_file(self):
        filename = "double.txt"
        try:
            with open(filename, 'w') as file:
                for square in self.even_squared:
                    file.write(f"{square}\n")
            return True
        except Exception as error:
            print(f"An error occurred while writing to '{filename}': {error}")
            return False

    def write_triple_file(self):
        filename = "triple.txt"
        try:
            with open(filename, 'w') as file:
                for cube in self.odd_cubed:
                    file.write(f"{cube}\n")
            return True
        except Exception as error:
            print(f"An error occurred while writing to '{filename}': {error}")
            return False

    def process(self):
        if not self.read_integers():
            return False
        if not self.classify_and_transform():
            return False
        if not self.write_double_file():
            return False
        if not self.write_triple_file():
            return False
        print("Processing completed successfully.")
        return True
