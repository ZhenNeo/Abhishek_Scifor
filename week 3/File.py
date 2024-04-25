def check_numerical_values(file_path):
    try:
        # Open the file for reading
        with open(file_path, 'r') as file:
            # Read lines from the file
            lines = file.readlines()

        # Check each line for numerical values
        for line_number, line in enumerate(lines, start=1):
            if any(char.isdigit() for char in line):
                print(f"Line {line_number}: {line.strip()}")

        print("Numerical values checked successfully.")

    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Example usage
file_path = 'D:/Python projects/Scifor/aboutPython.txt'  # Replace with the actual file path
check_numerical_values(file_path)
