"""
Create a program that ask user for a question, it will also ask for 4 possible answer (a,b,c,d)
and the correct answer.Write the collected data to a text file.
Ask another question until the user chose to exit.
"""

#use the function open() to create the text file

#ask the user for their name, after asking the user for their name, display text that will prompt them to
#write a quiz question and let the user input 4 different answers to the question with 1 being the correct
#answer.

#make a "Next question" functionality using the while loop, make it go on until the user tells the program
#to stop.

f = open("user_quiz","w")
user_name = input("Please enter your name: ")

if user_name: #Checks whether the variable is empty or not, runs when not empty
    while True:
        user_question = input("Please input a quiz question: ")
        with open("user_quiz", "a") as f:
            f.write("Question: " + str(user_question + "\n"))

        user_choice1 = input("Please enter a quiz choice: ")
        with open("user_quiz", "a") as f:
            f.write("Answer A: " + str(user_choice1+ "\n"))

        user_choice2 = input("Please enter a quiz choice: ")
        with open("user_quiz", "a") as f:
            f.write("Answer B: " + str(user_choice2 + "\n"))

        user_choice3 = input("Please enter a quiz choice: ")
        with open("user_quiz", "a") as f:
            f.write("Answer C: " + str(user_choice3 + "\n"))

        user_choice4 = input("Please enter a quiz choice: ")
        with open("user_quiz", "a") as f:
            f.write("Answer D: " + str(user_choice4 + "\n"))


        while True:
            user_answer = input("What is the correct answer for the question? (A, B, C, D): ")
            valid_answer = ["A", "B", "C", "D"]

            if user_answer in valid_answer:
                break
            else:
                print("That is not a valid answer please try again: ")

        with open("user_quiz", "a") as f:
            f.write("Correct answer: " + str(user_answer + "\n"))

        user_exit = input("Do you want to input another question? Y/N: ").lower()
        if user_exit[0] == "n":
            break




f = open("user_quiz", "r")
print(f.read())
