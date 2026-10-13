import sys
import os

# Absolute path for the output file
output_file = "/Users/tobyowen/Documents/Coding/You Exist/output.txt"

# Open the file in write mode
with open(output_file, "w") as f:
    # Redirect stdout to the file
    sys.stdout = f
    # code goes here - HOW DO I MAKE IT SO THAT YOU STILL SEE EVERYTHING IN THE TERMINAL, BUT 
