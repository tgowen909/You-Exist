import sys
from rich import print as p

class Tee:
    def __init__(self, *files):
        self.files = files

    def write(self, text):
        for file in self.files:
            file.write(text)
            file.flush()  # Ensure data is written immediately

    def flush(self):
        for file in self.files:
            file.flush()

# Define the output file name
output_file = "output.txt"

# Open the file in append mode
f = open(output_file, "a")

# Create an instance of Tee to duplicate the output to both sys.stdout and the file
tee = Tee(sys.stdout, f)

# Redirect sys.stdout to the Tee object
sys.stdout = tee

# Your Python script code here
print("This is the output of my Python script.")
p("It will be written to both the terminal and the output file.", "bold red")

# Example of using the custom input function
name = input("Enter your name: ")

# Log a newline (Enter)
f.write('\n')

# Close the file when the program is finished
f.close()

# Restore sys.stdout to its original state
sys.stdout = sys.__stdout__
