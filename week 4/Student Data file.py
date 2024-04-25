import os

def create_student_file(student_name): # Create a new file for the student and initialize with an empty list
    file_name = f"{student_name}_transactions.txt"
    with open(file_name, 'w') as file:
        file.write("[]")
    print(f"File created for {student_name}: {file_name}")

def read_student_file(student_name): # Read and display the transactions from the student's file
    file_name = f"{student_name}_transactions.txt"
    if os.path.exists(file_name):
        with open(file_name, 'r') as file:
            transactions = eval(file.read())
        print(f"Transactions for {student_name}: {transactions}")
    else:
        print(f"File not found for {student_name}")

def append_transaction(student_name, new_transaction): # Append a new transaction to the student's file
    file_name = f"{student_name}_transactions.txt"
    if os.path.exists(file_name):
        with open(file_name, 'r') as file:
            transactions = eval(file.read())
        transactions.append(new_transaction)
        with open(file_name, 'w') as file:
            file.write(str(transactions))
        print(f"New transaction added for {student_name}")
    else:
        print(f"File not found for {student_name}")

def rename_student_file(student_name, new_name): # Rename the student's file
    old_file_name = f"{student_name}_transactions.txt"
    new_file_name = f"{new_name}_transactions.txt"
    if os.path.exists(old_file_name):
        os.rename(old_file_name, new_file_name)
        print(f"File renamed from {old_file_name} to {new_file_name}")
    else:
        print(f"File not found for {student_name}")

def delete_student_file(student_name): # Delete the student's file
    file_name = f"{student_name}_transactions.txt"
    if os.path.exists(file_name):
        os.remove(file_name)
        print(f"File deleted for {student_name}")
    else:
        print(f"File not found for {student_name}")

student_name = "Ryan Reynolds"
create_student_file(student_name)
read_student_file(student_name)
new_transaction = "Graduated to Grade 8"
append_transaction(student_name, new_transaction)
new_name = "DeadPool"
rename_student_file(student_name, new_name)
read_student_file(new_name)
delete_student_file(new_name)
