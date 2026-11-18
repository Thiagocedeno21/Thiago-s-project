#this is the start of my project


# Welcome message
print("================================")
print("   WELCOME TO THE QUESTION CHALLENGE GAME!")
print("================================")
print("You will answer 10 questions.")
print("Categories: Mathematics and Sports")
print("Each correct answer earns 1 point.")

# Sport questions
sports_questions = [
    ("How many players are on a soccer team?", "11"),
    ("Which sport uses a racket?", "tennis"),
    ("Which sport uses a puck?", "hockey"),
    ("How many rings are on the Olympic flag?", "5"),
    ("Which sport does Messi play?", "soccer"),
    ("How many points is a touchdown worth in American football?", "6"),
    ("Which country invented judo?", "japan"),
    ("How many players are on a basketball team on the court?", "5"),
    ("What sport is played at Wimbledon?", "tennis"),
    ("How many holes are in a standard round of golf?", "18")
]

# Mathematics questions
math_questions = [
    ("What is 8 + 7?", "15"),
    ("What is 20 - 9?", "11"),
    ("What is 6 x 4?", "24"),
    ("What is 36 divided by 6?", "6"),
    ("What is 9 x 8?", "72"),
    ("What is 45 + 27?", "72"),
    ("What is 100 - 46?", "54"),
    ("What is 12 x 12?", "144"),
    ("What is half of 86?", "43"),
    ("What is the square of 7?", "49")
]

# Pick the category
print("\n1. Mathematics")
print("2. Sports")
print("3. Both")

category = input("Choose 1, 2, or 3: ")

if category == "1":
    questions = math_questions
elif category == "2":
    questions = sports_questions
elif category == "3":
    questions = math_questions + sports_questions
else:
    print("Invalid choice! Please run the game again and choose 1, 2, or 3.")
    questions = []

# Play the game
score = 0

for question, answer in questions:
    print("\n" + question)
    player_answer = input("Your answer: ")

    if player_answer.strip().lower() == answer.lower():
        print("Correct!")
        score = score + 1
    else:
        print("Wrong! The correct answer is:", answer)

# Display final score
print("\n================================")
print("GAME OVER!")
print("Your final score is:", score, "/", len(questions))
print("================================")
