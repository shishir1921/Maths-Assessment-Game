import random


def extreme_mode(num_questions):
    score = 0
    min_num, max_num, allowed_operators = 1, 100, ['+', '-', '*', '/']

    i = 0  # Initialize question counter outside the loop

    while num_questions == 0 or i < num_questions:  # Loop until quit or num_questions reached
        while True:  # Loop until a valid answer is given
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
                while num2 == 0:  # Avoid division by zero
                    num2 = random.randint(min_num, max_num)
                answer = round(num1 / num2, 2)

            # Check for quit command before other validations
            user_answer = input(question)
            if user_answer.lower() == 'quit':
                print(f"You quit the game. Your final score is {score}/{i}.")  # Use i for actual questions asked
                return score

            if not user_answer:  # Check for empty input
                print("Please enter an answer.\n")
                continue

            try:
                user_answer = float(user_answer)
                if user_answer == answer:
                    score += 1
                    print("Correct!\n")
                else:
                    print(f"Wrong! The correct answer is {answer}.\n")
                break
            except ValueError:
                print("Invalid answer. Please enter a number.\n")

        i += 1  # Increment the question counter only if a valid answer is provided

    print(f"Your final score is {score}/{i}.")  # Use i for the final score as well
    return score
