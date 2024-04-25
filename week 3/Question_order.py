def sort_questions(question_list): # sorting the list without using inbuilt function
    n = len(question_list)

    for i in range(n):
        for j in range(0,n-i-1):
            if question_list[j] > question_list[j+1]:
                question_list[j], question_list[j+1] = question_list[j+1], question_list[j]

def questions(): # Part 1
    question_list = []
    n = int(input("Enter the nunber of questions: "))

    for i in range(n):
        user_input = float(input(f"Enter question number {i + 1}: "))
        question_list.append(user_input)
    
    sort_questions(question_list)

    print("Question numbers", question_list)
    return question_list
    
def find_page_number(selected_questions, question_number): # Part 2
    if question_number in selected_questions:
        page_number = selected_questions.index(question_number) + 1
        print(f"Solve it on page number {page_number}.")
    else:
        print("You don't have to solve this question.")

def main(): 
    selected_questions = questions()
    question_number = int(input("Enter question number: "))

    find_page_number(selected_questions,question_number)

main()