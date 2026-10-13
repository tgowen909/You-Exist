import os

# Absolute path of the file
absolute_path = '/Users/tobyowen/Documents/Coding/You Exist/Audio/Crazy_Dave.mp3'

# Current working directory
current_directory = os.getcwd()

# Relative path from current directory to the file
relative_path = os.path.relpath(absolute_path, current_directory)

print("Relative path:", relative_path)
