def numeric(filepath):
    try:
        # Open the file for reading
        with open(filepath,"r") as file: 
            # Read lines from the file
            content = file.readlines()

        # Check each line for numerical values
        for line, word in enumerate(content, start=1):
            if any(char.isdigit() for char in word):
                print(f"Line {line}: {word.strip()}")

    except FileNotFoundError: 
        print("file {filepath} not found")        

filepath = 'D:/Python projects/Scifor/aboutPython.txt'
numeric(filepath)