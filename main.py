# Show the Fun Title
print(r"""

  /$$$$$$            /$$                  /$$$$$$  /$$                              
 /$$__  $$          |__/                 /$$__  $$| $$                              
| $$  \ $$ /$$   /$$ /$$ /$$$$$$$$      | $$  \__/| $$$$$$$   /$$$$$$  /$$  /$$  /$$
| $$  | $$| $$  | $$| $$|____ /$$/      |  $$$$$$ | $$__  $$ /$$__  $$| $$ | $$ | $$
| $$  | $$| $$  | $$| $$   /$$$$/        \____  $$| $$  \ $$| $$  \ $$| $$ | $$ | $$
| $$/$$ $$| $$  | $$| $$  /$$__/         /$$  \ $$| $$  | $$| $$  | $$| $$ | $$ | $$
|  $$$$$$/|  $$$$$$/| $$ /$$$$$$$$      |  $$$$$$/| $$  | $$|  $$$$$$/|  $$$$$/$$$$/
 \____ $$$ \______/ |__/|________/       \______/ |__/  |__/ \______/  \_____/\___/ 

""")

# Display the rules of the game
print("Welcome to Quiz Show, where we ask only true or false questions. For each of the three questions, please enter the letter T or F. Good luck! ")
print()

# Store your questions and your True/False answers two tuples
questions = ("Q1. Baltimore is the capital of Maryland", "Q2. The Mississippi River is the longest river in the world", "Q3. Michael Jackson is considered the King of Pop")
answers = ("F", "F", "T")
userAnswer = ""
numberOfQuestions = len(questions)
count = 0

# Display each question to the user one at a time
for index in range(numberOfQuestions):
  
  print(questions[index])
  
  while(userAnswer != "T" and userAnswer != "F"):

    # Ask the user to put in a T or F only, or it will ask again
    userAnswer = input("Enter a 'T' for True and an 'F' for False: ")

    # Keep track of the answer if it's correct
    if(userAnswer == answers[index]):
      count += 1
  
  # Reset the user's answer for each question  
  userAnswer = ""
  print()

# the number of questions the user got right out of total number of questions.
print(f"You got {count} out of {numberOfQuestions} correct! Thanks for playing!")