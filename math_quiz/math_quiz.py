import random


def random_Number_Generator(min, max):
    """
    Defining the random number generator function that returns a random number between the specified range.
    """
    return random.randint(min, max) # min is the minimum value and max is the maximum value of our desired range

def random_Operator_Generator():
    """
    Defining the random operator generator function that returns a random operator from the list ['+', '-', '*'].
    """
    return random.choice(['+', '-', '*'])

def math_Problem_Solution_Generator(number1, number2, operator):
    """
    Defining the basic calaculator function that takes two numbers and an operator as input and returns the problem and the answer as a tuple.
    """
    # Using f string to format the problem
    problem = f"{number1} {operator} {number2}"
    # Using if else statements to calculate the answer based on the operator
    if operator == '+': answer = number1 + number2 # This was a bug, it should be number1 + number2
    elif operator == '-': answer = number1 - number2 # This was a bug, it should be number1 - number2
    else: answer = number1 * number2 # As we have only three operators, we can use else statement to calculate the answer for the multiplication operator
    return problem, answer

def math_quiz():
    """
    This function starts the math quiz game in which users will be prompted with random math problems 
    and if they provide correct solution they will earn a point. The score is calculated as a proportion 
    of the correct answers to the total questions.
    """
    score = 0 #initializing score with 0
    total_questions = 5 # Defining to control iterations
    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")
    # The loop runs for the total number of questions i.e., it will randomly promopt question for the user.
    for _ in range(total_questions):
        number1 = random_Number_Generator(1, 10) 
        number2 = random_Number_Generator(1, 5) # This was a bug, it should be an integer value not float.
        operator = random_Operator_Generator()
        # Saving the problem and the answer in the variables PROBLEM and ANSWER as a tuple
        PROBLEM, ANSWER = math_Problem_Solution_Generator(number1, number2, operator)
        # Displaying the problem to the user
        print(f"\nQuestion: {PROBLEM}")
        # using try-catch block to handle the exception if the user enters a non-integer value
        try:
            # Taking the input from the user and converting it to integer
            useranswer = int(input("Your answer: "))
            # Checking if the user answer is correct
            if useranswer == ANSWER:
                print("Correct! You earned a point.")
                # Rewarding user with a point
                score += 1 # This is a bug, it should be s += 1
            else:
                print(f"Wrong answer. The correct answer is {ANSWER}.")
        # Handling the exception if the user enters a non-integer value    
        except ValueError:
            print("Type Error! Please enter an integer.")
    # Displaying the final score to the user
    print(f"\nGame over! Your score is: {score}/{total_questions}")

if __name__ == "__main__":
    math_quiz()
