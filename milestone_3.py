import random

# Create a list containing the names of your 5 favorite fruits.
favorite_fruits = ["Apple", "Banana", "Orange", "Grapes", "Mango"]

# Assign this list to a variable called word_list.
word_list = favorite_fruits

# Create the random.choice method and pass the word_list variable into the choice method.
word = random.choice(word_list)

# Print out the newly created list to the standard output (screen).
print("Word List:", word_list)

# Define the check_guess function
def check_guess(guess):
    # Step 2: Convert the guess into lower case.
    guess = guess.lower()
    
    # Step 3: Move the code to check if the guess is in the word into this function block.
    if guess in word:
        return True
    else:
        return False

# Define the ask_for_input function
def ask_for_input():
    # Step 2: Move the code to check if the input is a valid guess into this function block.
    while True:
        guess = input("Guess a letter: ")

        if len(guess) == 1 and guess.isalpha():
            # Step 3: Outside the while loop, call the check_guess function to check if the guess is in the word.
            if check_guess(guess):
                print(f"Good guess! {guess} is in the word.")
            else:
                print(f"Sorry, {guess} is not in the word. Try again.")
            break
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")

# Step 4: Outside the function, call the ask_for_input function to test your code.
ask_for_input()
