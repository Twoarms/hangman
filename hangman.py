import random
HANGMAN_PICS = ['''
 +---+
   |
   |
   |
   ===''','''
 +---+
 O |
   |
   |
   ===''','''
 +---+
 O |
 | |
   |
   ===''','''
 +---+
 O |
/| |
   |
   ===''','''
 +---+
 O |
/|\|
   |
   ===''','''
 +---+
 O |
/|\|
/  |
   ===''','''
 +---+
 O |
/|\|
/ \|
   ===''']

words = 'fourmi babouin ours castor cobra cougar coyote corbeau cerf chien canard aigle renard grenouille faucon lion lezard singe souris louttre chouette panda perroquet pigeon python lapin saumon requin mouton paresseux tigre truite dinde tortue loup zebre'.split()

def getRandomWord(wordList):
    wordIndex = random.randint(0, len(wordList)-1)
    return wordList[wordIndex]

def displayBoard(missedLetters, correctLetters, secretWord):
    print(HANGMAN_PICS[len(missedLetters)])
    print()

    print('Mauvaises lettres:', end=' ')
    for letter in missedLetters:
        print(letter, end=' ')
    print()

    blanks = '_'*len(secretWord)

    for i in range(len(secretWord)):
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]

    for letter in blanks:
        print(letter, end=' ')
    print()

def getGuess(alreadyGuessed):
    while True:
        print('Entrez une lettre, svp.')
        guess = input()
        guess = guess.lower()
        if len(guess) !=1:
            print('Entrer une seule lettre, svp.')
        elif guess in alreadyGuessed:
            print('Vous avez déjà entré cette lettre. Choisissez en une autre.')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('Une LETTRE, svp.')
        else:
            return guess

def playAgain():
    print('Voulez-vous rejouer ? (oui ou non)')
    return input().lower().startswith('o')

print('P E N D U')
missedLetters = ''
correctLetters = ''
secretWord = getRandomWord(words)
gameIsDone = False

while True:
    displayBoard(missedLetters, correctLetters, secretWord)

    guess = getGuess(missedLetters + correctLetters)

    if guess in secretWord:
        correctLetters = correctLetters + guess

        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break
            
        if foundAllLetters:
                print('Oui! Le mot secret est bien "' + secretWord + '"! C\'est gagné !')
                gameIsDone = True
                
    else:
        missedLetters = missedLetters + guess

        if len(missedLetters) == len(HANGMAN_PICS) - 1:
            displayBoard(missedLetters, correctLetters, secretWord)
            print('Vous avez perdu...\nAvec' + str(len(missedLetters)) + 'mauvaises lettres et '+ str(len(correctLetters)) + 'bonnes lettres, le mot secret était "' + secretWord + '"')
            gameIsDone = True

    if gameIsDone:
        if playAgain():
            missedLetters = ''
            correctLetters = ''
            gameIsDone = False
            secretWord = getRandomWord(words)
        else:
            break
