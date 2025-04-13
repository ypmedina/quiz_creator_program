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

f = open("user_quiz","x")
user_name = input("Please enter your name: ")

if user_name: #Checks whether the variable is empty or not, runs when not empty
    while True:
        try:
            user_question = input("Please input a quiz question: ")
            with open("user_quiz", "a") as f:
                f.write(str(user_name))
        

        except ValueError:
            print(" ")


print(f.read())
