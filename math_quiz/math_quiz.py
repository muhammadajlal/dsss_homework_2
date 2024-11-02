import random


def random_Number_Generator(min, max):
    """
    Generate a random integer within a specified range.
    
    Args:
    - min (int): Minimum value of the range.
    - max (int): Maximum value of the range.
    
    Returns:
    - int: Random integer within the range [min, max].
    """
    return random.randint(min, max) # min is the minimum value and max is the maximum value of our desired range

def random_Operator_Generator():
    """
    Select a random operator from a list of math operators.
    
    Returns:
    - str: A random operator, one of the list ['+', '-', or '*'].
    """
    return random.choice(['+', '-', '*'])

def math_Problem_Solution_Generator(number1, number2, operator):
    """
    Generate a math problem string and calculate the answer based on given integers and operator.
    
    Args:
    - number1 (int): The first operand.
    - number2 (int): The second operand.
    - operator (str): The operator ('+', '-', or '*') used in the problem.
    
    Returns:
    - tuple: The problem as a string and the correct answer as an integer.
    """
    # Using f string to format the problem
    problem = f"{number1} {operator} {number2}"
    # Using if else statements to calculate the answer based on the operator
    if operator == '+': answer = number1 + number2 # This was a bug, it should be number1 + number2
    elif operator == '-': answer = number1 - number2 # This was a bug, it should be number1 - number2
    else: answer = number1 * number2 # As we have only three operators, we can use else statement
    return problem, answer

def math_quiz():
    """
    Starts a math quiz game where users are prompted with random math problems and earn points for correct answers. 
    If the user provides the correct answer, he earn a point. The final score is displayed as the number of correct 
    answers out of the total questions.

    Args:
    - None
    
    Raises:
        ValueError: If the user inputs a non-integer value when prompted for an answer.

    Returns:
    - None
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
        # Incorporating a while loop so that user can try again if he enters a non-integer value
        while True:
            # Displaying the problem to the user
            print(f"\nQuestion: {PROBLEM}")
            # using try-catch block to handle the exception if the user enters a valid input value (integer)
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
                break
                # Handling the exception if the user enters a non-integer value    
            except ValueError:
                print("Value Error! Please enter an integer.")
    # Displaying the final score to the user
    print(f"\nGame over! Your score is: {score}/{total_questions}")

# Definig the main function to give setup.py file an entry point to run the game
def main():
    math_quiz()

if __name__ == "__main__":
    main()
