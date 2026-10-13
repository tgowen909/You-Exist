with open("other_file.py") as f:
    code = f.read()
    exec(code)
