import os
import requests

word = ""               # Create word variable
allResults = list()     # Create results list to store all guesses

# Function that returns whether a word exists
def is_valid_word(word):
    response = requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}")  # Check if word is valid by pinging some dictionary
    return response.status_code == 200                                                  # Passes on the service's response

while len(word) != 5 or not is_valid_word(word.lower()):    # Repeats until word is 5 letters and valid
    os.system("cls" if os.name == "nt" else "clear")        # Clears the screen
    word = input("Enter a five-letter word: ")              # Asks for input

for attempt in range(0,6):      # Main loop
    guess = ""                  # Reset 'guess' variable

    while len(guess) != 5 or not is_valid_word(guess.lower()):  # Repeats until guess is 5 letters and valid
        os.system("cls" if os.name == "nt" else "clear")        # Clears screen
        if allResults != list():
            print("\n".join(map(str, allResults)))                  # (Re)prints results
        guess = input(f"\033[100m     \n\033[0m"*(-attempt+6))      # Asks for input

    guessResult = list()                                # Create results list to store a single guess

    for positionIndex in range(0,5):
        selectedGuessLetter = guess[positionIndex]  # Cycles through every letter in the guess
        guessIndex = positionIndex                  # Passes value to different variable (Not really necessary but didn't feel like changing it)
        isGrey = True                       # Resets flag
        squareTaken = False                 # Resets flag
        
        for position in range(0,5):
            selectedWordLetter = word[position]         # Cycles through every letter in the word to compare it to the letter selected from the guess

            if selectedWordLetter == selectedGuessLetter:   # Compares selected letter from the word to selected letter from the guess 
                if guessIndex == position:                  # Check if the position of the letter in the guess is the same as the one in the word
                    if squareTaken == False:
                        guessResult.append(f"\033[42m{selectedGuessLetter}\033[0m")     # Append green square to guessResult
                        isGrey = False                                                  # Update flag so no grey square is appended
                        squareTaken = True                                              # Update backup flag that locks the square in
                elif guessIndex != position:                # Backup position check
                    if squareTaken == False:
                        guessResult.append(f"\033[43m{selectedGuessLetter}\033[0m")     # Append yellow square to guessResult
                        isGrey = False                                                  # Update flag so no grey square is appended
                        squareTaken = True                                              # Update backup flag that locks the square in

        if isGrey == True:                                                      # Check flag if square should be grey
            if squareTaken == False:                                            # Check flag if square should be appended
                guessResult.append(f"\033[100m{selectedGuessLetter}\033[0m")
                squareTaken = True                                              # Update backup flag that locks the square in

    os.system("cls" if os.name == "nt" else "clear")    # Clear screen for result printing

    guess_string = str("".join(map(str, guessResult)))  # Convert the guessResult list to a string
    allResults.append(guess_string)                     # Append the newly created string to a list
    print("\n".join(map(str, allResults)))              # Print all the results below each other
    if guess == word:                           # Checks if game should be won
        print("Great")                          # Print complemetary congratulatory message
        break
    if attempt == 5:                            # Checks if game over message should be printed
        print(f"Too bad\nThe word was {word}")  # Print what the word was so the player isn't left questioning their life
        break
