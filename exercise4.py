#("exercise_4\n")

print("Welcome to the European Capitals Quiz!")
print("Answer the following questions:\n")

questions = [
    ("What is the capital of France?", "Paris"),
    ("What is the capital of Germany?", "Berlin"),
    ("What is the capital of Italy?", "Rome"),
    ("What is the capital of Spain?", "Madrid"),
    ("What is the capital of Portugal?", "Lisbon"),
    ("What is the capital of Netherlands?", "Amsterdam"),
    ("What is the capital of Belgium?", "Brussels"),
    ("What is the capital of Sweden?", "Stockholm"),
    ("What is the capital of Poland?", "Warsaw"),
    ("What is the capital of Greece?", "Athens")
]#includes all the questions for the entire quiz 
score = 0

for question, correct_answer in questions:
    user_answer = input(question + " ")
    
    if user_answer.lower() == correct_answer.lower():#ignores capitalization and accepts answers regardless of wrong capitalizations
        print("Correct!")
        score += 1
    else:
        print(f"Wrong! The correct answer is {correct_answer}.")
    
    print()

print(f"Quiz completed! Your score: {score}/10")
if score == 10:
    print("Perfect, 10/10!")
elif score >= 9:
    print("(9/10")
elif score >= 8:
    print("8/10")
elif score >= 7:
    print("7/10")
elif score >= 6:
    print("6/10")
elif score >= 5:
    print("5/10")
else:
    print("Keep Practicing")#a small and simple scoreboard addition to the quiz