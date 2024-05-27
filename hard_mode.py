import random

def generate_question(min_num, max_num, allowed_operators):
    num1 = random.randint(min_num, max_num)
    num2 = random.randint(min_num, max_num)
    operator = random.choice(allowed_operators)
    question = f"What is {num1} {operator} {num2}? "

    if operator == '+':
        answer = num1 + num2
    elif operator == '-':
        answer = num1 - num2
    elif operator == '*':
        answer = num1 * num2
    else:  # operator == '/'
        while num2 == 0:
            num2 = random.randint(min_num, max_num)
        answer = round(num1 / num2, 2)

    return question, answer

def hard_mode(num_questions):
    score = 0
    min_num, max_num, allowed_operators = 1, 25, ['+', '-', '*']

    for i in range(num_questions):
        while True:  # Loop until a valid answer is given
            question, correct_answer = generate_question(min_num, max_num, allowed_operators)
            user_answer = input(question)

            if not user_answer:  # Check for empty input
                print("Please enter an answer.\n")
                continue

            try:
                user_answer = float(user_answer)
                if user_answer == correct_answer:
                    score += 1
                    print("Correct!\n")
                else:
                    print(f"Wrong! The correct answer is {correct_answer}.\n")
                break  # Exit the inner loop if the answer is valid
            except ValueError:
                print("Invalid answer. Please enter a number.\n")

    print(f"Your final score is {score}/{num_questions}.")

    return score