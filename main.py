import easy_mode
import medium_mode
import hard_mode
import extreme_mode

GAME_HISTORY_FILE = 'game_history.txt'

def main():
    anonymous_count = 0
    user = None
    game_history = load_game_history()

    while user is None:
        user_input = input("Hey, what's your name? ")
        if user_input.strip():
            user = user_input
            print(f"\nNice to meet you, {user}!\n")
        else:
            anonymous_count += 1
            if anonymous_count == 2:
                user = "Anonymous"
                print("\nYou've chosen to be anonymous. Welcome!\n")
            else:
                print("Please enter a valid input.\n")

    while True:
        show_instructions = input('Do you want to read the instructions of this game? (yes/no): ')
        if show_instructions.lower() in ['yes', 'no']:
            break
        print('Please type in yes or no.\n')

    if show_instructions.lower() == 'yes':
        with open('instructions.txt') as f:
            print(f.read())

    print('\nNow select the difficulty mode:\nEasy\nMedium\nHard\nExtreme\n')

    while True:
        user2 = input('Please type in the difficulty level you want to play from the above options: ')
        if user2.lower() in ['easy', 'medium', 'hard', 'extreme']:
            break
        print("Invalid difficulty level. Please choose from Easy, Medium, Hard, or Extreme.\n")

    num_questions = get_num_questions(user2.lower())

    if user2.lower() == 'easy':
        score = easy_mode.easy_mode(num_questions)
    elif user2.lower() == 'medium':
        score = medium_mode.medium_mode(num_questions)
    elif user2.lower() == 'hard':
        score = hard_mode.hard_mode(num_questions)
    elif user2.lower() == 'extreme':
        score = extreme_mode.extreme_mode(num_questions)

    # Update and display game history
    update_game_history(user, user2.lower(), num_questions, score)
    display_game_history()

def get_num_questions(mode):
    while True:
        try:
            if mode == 'extreme':
                num_questions = int(input("Enter the number of questions you want (or 0 for unlimited): "))
                if num_questions >= 0:
                    return num_questions
            else:
                min_questions, max_questions = {
                    'easy': (1, 10),
                    'medium': (10, 25),
                    'hard': (25, 50)
                }[mode]
                num_questions = int(
                    input(f"Enter the number of questions (between {min_questions} and {max_questions}): "))
                if min_questions <= num_questions <= max_questions:
                    return num_questions
        except ValueError:
            pass
        print("Invalid input. Please enter a valid number.\n")


def load_game_history():
    game_history = []
    try:
        with open(GAME_HISTORY_FILE, 'r') as f:
            for line in f:
                name, mode, questions, score = line.strip().split(',')
                game_history.append((name, mode, int(questions), int(score)))
    except FileNotFoundError:
        pass
    return game_history

def display_game_history():
    game_history = load_game_history()  # Reload to get the latest history
    if game_history:
        print("\n--- Game History (Last 5 Games) ---")
        print("Name\tMode\t  Questions  \tScore")
        for name, mode, questions, score in game_history[-5:]:
            if mode == "extreme" and questions == 0:
                questions_str = "∞"  # Display infinity symbol for unlimited questions
            else:
                questions_str = str(questions)
            print(f"{name}\t{mode}\t{questions_str:^12}\t{score:^5}")

def update_game_history(name, mode, questions, score):
    game_history = load_game_history()
    game_history.append((name, mode, questions, score))
    if len(game_history) > 5:
        game_history.pop(0)
    save_game_history(game_history)

def save_game_history(game_history):
    with open(GAME_HISTORY_FILE, 'w') as f:
        for name,   mode, questions, score in game_history:
            f.write(f"{name},{mode},{questions},{score}\n")


if __name__ == "__main__":
    main()