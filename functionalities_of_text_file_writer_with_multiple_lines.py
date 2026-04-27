class TextFileWriter:
    def __init__(self, filename="mylife.txt"):
        slef.filename = filename
        self.content = []

    def get_user_input(self):
        while True:
            line = input("Enter a line of text (or 'done' to finish): ")
            if line.lower() == 'done':
                break
            self.content.append(line)
            print(f"Added: '{line}'")
            else:
                print("Invalid input. Please enter a line of text or 'done' to finish.")

            more = input(
                "Do you want to add more lines? (yes/no): ").strip().lower()
            if more in ['no', 'n', '']:
                break

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
