def count_file_stats(file_path):
    total_lines = 0
    total_words = 0
    total_letters = 0
    lines_starting_with_letter = {}

    with open(file_path, 'r') as file:
        for line in file:
            total_lines += 1
            total_words += len(line.split())
            total_letters += len(line)
            first_letter = line.strip()[0].lower()
            lines_starting_with_letter[first_letter] = lines_starting_with_letter.get(first_letter, 0) + 1
    return total_lines, total_words, total_letters, lines_starting_with_letter

def main():
    file_path = 'D:/python projects/Scifor/assessment.txt'  # Change this to your file path
    total_lines, total_words, total_letters, lines_starting_with_letter = count_file_stats(file_path)

    print(f"Total number of lines: {total_lines}")
    print(f"Total number of words: {total_words}")
    print(f"Total number of letters: {total_letters}")
    print("\nLines starting with each letter:")
    for letter, count in sorted(lines_starting_with_letter.items()):
        print(f"{letter.upper()}: {count}")

if __name__ == "__main__":
    main()
