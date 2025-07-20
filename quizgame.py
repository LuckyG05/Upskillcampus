# quizgame.py

# Quiz Questions [question, option1, option2, option3, option4, correct_option_number]
questions = [
    ["Which planet is known as the RED PLANET?", "Venus", "Earth", "Mars", "Jupiter", 3],
    ["Which is the longest river in the world?", "Amazon", "Nile", "Mississippi", "Yangtze", 2],
    ["What is the capital of Japan?", "Beijing", "Tokyo", "Seoul", "Bangkok", 2],
    ["What gas is used to extinguish fires?", "Oxygen", "Hydrogen", "Carbon dioxide", "Nitrogen", 4],
    ["What chemical element is designated as Hg?", "Silver", "Tin", "Copper", "Mercury", 4],
    ["Which is the largest island?", "New Guinea", "Andaman Nicobar", "Greenland", "Hawaii", 3],
    ["Which city is known as the Silicon Valley of India?", "Bangalore", "Chennai", "Hyderabad", "Mumbai", 1],
    ["Which of the following is NOT a neighboring country of India?", "Bhutan", "Thailand", "Nepal", "China", 2],
    ["How many sides does a decagon have?", "Eight", "Seven", "Nine", "Ten", 4],
    ["What is the speed of light?", "3 x 10^2 m/s", "3 x 10^8 m/s", "8 x 10^8 m/s", "6 x 10^8 m/s", 2]
]

def ask_question(question):
    print("\n" + question[0])
    print(f"1. {question[1]}")
    print(f"2. {question[2]}")
    print(f"3. {question[3]}")
    print(f"4. {question[4]}")

    while True:
        try:
            choice = int(input("Enter your answer (1-4): "))
            if 1 <= choice <= 4:
                return choice
            else:
                print("Please choose a number between 1 and 4.")
        except ValueError:
            print("Invalid input! Please enter a number (1-4).")

def save_score(name, score, total):
    with open("scoreboard.txt", "a") as file:
        file.write(f"{name}: {score}/{total}\n")

def display_scoreboard():
    print("\n--- Previous Scores ---")
    try:
        with open("scoreboard.txt", "r") as file:
            print(file.read())
    except FileNotFoundError:
        print("No previous scores found.")

def run_quiz():
    print("Welcome to the Quiz Game!")
    play = input("Do you want to play? (Y/N): ")

    if play.lower() not in ["y", "yes"]:
        print("See you next time!")
        return

    name = input("Enter your name: ")
    score = 0

    for question in questions:
        user_choice = ask_question(question)
        if user_choice == question[5]:
            print("Correct Answer!")
            score += 1
        else:
            print(f"Oops, wrong answer! Correct answer was option {question[5]}")
        print(f"Current Score: {score}")
        print("-" * 30)

    print(f"\n{name}, your total score is: {score}/{len(questions)}")
    save_score(name, score, len(questions))
    display_scoreboard()
    print("Thanks for playing!")

# Run the game
if __name__ == "__main__":
    run_quiz()
