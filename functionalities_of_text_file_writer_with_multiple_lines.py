class TextFileWriter:
    def __init__(self, filename="mylife.txt"):
        self.filename = filename
        self.content = []

    def get_user_input(self):
        while True:
            line = input("Enter a line of text (or 'done' to finish): ")

            if line.lower() == 'done':
                break

            if line:
                self.content.append(line)
                print(f"Added: '{line}'")
            else:
                print("Invalid input. Please enter a line of text or 'done' to finish.")

            more = input(
                "Do you want to add more lines? (yes/no): ").strip().lower()
            if more in ['no', 'n', '']:
                break
        return len(self.content) > 0

    def write_to_file(self):
        if not self.content:
            print("No content to write. Please add some lines first.")
            return False

        try:
            with open(self.filename, 'w') as file:
                for line in self.content:
                    file.write(line + '\n')

            print(f"Content successfully written to '{self.filename}'")
            return True

        except Exception as error:
            print(f"An error occurred while writing to the file: {error}")
            return False

    def display_file_content(self):
        try:
            with open(self.filename, 'r') as file:
                print(f"\n Content of {self.filename}:")
                content = file.read()
                if content:
                    print(content)
                else:
                    print("The file is empty.")

        except FileNotFoundError:
            print(f"The file '{self.filename}' does not exist.")
        except Exception as error:
            print(f"An error occurred while reading the file: {error}")

    def process(self):
        if not self.get_user_input():
            print("No conent collected. Exiting.")
            return False

        confirm = input(
            "Do you want to write this content to the file? (yes/no): ").strip().lower()
        if confirm not in ['yes', 'y']:
            print("Writing cacelled to file.")
            return False

        if not self.write_to_file():
            print("Failed to write content to file.")
            return False

        self.display_file_content()

        print(f"\n Successfully completed writing to '{self.filename}'")
        return True
