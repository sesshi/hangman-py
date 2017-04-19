import random

#Game Loop
while True:
    attempts = 5
    won = False

    #Initialising and setting word
    wordArray = ["apples", "cats", "memory", "icecream", "black", "bicycle", "sandles"]
    word = random.choice(wordArray)
    print("Word contains {} letters".format(len(word)))
    print(len(word)*"_ ")
    print("You have {} attempts reamining".format(attempts))

    #displayWord determined by word length
    displayWord = []
    for space in word:
        displayWord.append("_")

    while attempts > 0 and won == False:
        userInput = raw_input("Enter a word to solve, or a letter to reveal:")

        if len(userInput) == 1: #Check Letter
            for index, letter in enumerate(word):
                if not displayWord[index].isalpha():
                    if userInput == word[index]:
                        #Append to new word array to display
                        displayWord[index] = userInput
                    else:
                        displayWord[index] = "_"
                else:
                    displayWord[index] = letter
            #Join array into a new string
            newWord = ' '.join(displayWord)
            print newWord

        else: #Check Word
            if userInput == word:
                won = True
                newWord = ' '.join(displayWord)
                print "Congratulations, you discovered the word!"
                break
            else:
                print "Guess incorrect."

        #Show attempts
        attempts -= 1
        print("You have {} attempts remaining.".format(attempts))

    #No more attempts message
    if attempts == 0 and won == False:
        print "You lost."

    #Restart Game
    restart = raw_input('\nWould you like to play again? y/n ')
    if restart == 'n':
        break
