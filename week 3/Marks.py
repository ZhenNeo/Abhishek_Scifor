def get_details():
    math = int(input("Enter Math marks: "))
    Science = int(input("Enter Science marks: "))
    English = int(input("Enter English marks: "))

    Student_details = {
        "Math": math,
        "Science": Science,
        "English": English
    }
    return Student_details

def main():
    details = {}
    for i in range(1,6):
        print(f"Enter details for student {i}")
        Student_details = get_details()
        details[f"Student {i}"] = Student_details
    display_details(details)

def display_details(details):
    for student, detail in details.items():
        print(f"\n{student} Details ")
        for subject, marks in detail.items():
            print(f"{subject} : {marks}")

main()
