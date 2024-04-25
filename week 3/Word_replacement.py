def word_replacenemt(filepath, target, replacement):
    with open(filepath, 'r') as file:
        content = file.read()
    
    modified_content = content.replace(target,replacement)

    with open(filepath, 'w') as file:
        file.write(modified_content)

filepath = 'Scifor/aboutPython.txt'
target = 'Pyhton'
replacement = 'Python'
word_replacenemt(filepath, target, replacement)