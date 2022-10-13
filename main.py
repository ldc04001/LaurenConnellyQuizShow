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

# Store your questions and your True/False answers two tuples
questions = ("Q1. Baltimore is the capital of Maryland", "Q2. The Mississippi River is the longest river in the world", "Q3. Michael Jackson is considered the King of Pop")
answers = ("F", "F", "T")
userAnswer = ""
numberOfQuestions = len(questions)

count = 0

# Display each question to the user
for index in range(numberOfQuestions):
  
  print(questions[index])

  while(userAnswer != ("T" or "F")):

    userAnswer = input("Enter a 'T' for True and an 'F' for False: ")
