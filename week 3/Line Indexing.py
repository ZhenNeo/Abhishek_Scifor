def line_Indexing(filepath):
    with open(filepath,'r') as file:
        lines = file.readlines()

    new_content = ''
    for line_number, line in enumerate(lines, start=1):
        new_content += str(line_number)+ ' ' + line
        
    with open(filepath,'w') as file:
        file.write(new_content)
    
filepath = 'Scifor/aboutPython.txt'
line_Indexing(filepath)