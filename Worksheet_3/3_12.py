class StringProcessor:
    def __init__(self):
        self.text = ""

    def get_String(self):
        self.text = input("Enter a string: ")

    def print_String(self):
        print(self.text.upper())

processor = StringProcessor()
processor.get_String()
processor.print_String()