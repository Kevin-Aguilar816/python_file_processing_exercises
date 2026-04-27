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
