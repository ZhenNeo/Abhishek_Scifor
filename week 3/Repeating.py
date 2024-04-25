def repeat(filepath):
    with open(filepath,'r') as file:
        content = file.read()
    
    words = content.split()
    unique_words = [words[0]]  # Initialize with the first word

    for i in range(1, len(words)):
        if words[i] != words[i - 1]:
            unique_words.append(words[i])
    new_content = ' '.join(unique_words)
    
    with open(filepath,'w') as file:
        file.write(new_content)

filepath = 'Scifor/aboutPython.txt'
repeat(filepath)    