def count_words(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()

        content = content.replace(',', ' ')
        words = content.split()
        num_words = len(words)

        print(f"Number of words in the file: {num_words}")
    except FileNotFoundError:
        print("File not found.")


file_path = 'Scifor/Healthy life.txt'
count_words(file_path)
