
def GetAnswerWithUnderscores(answer, letters_guessed):
    new = ''
    for items in answer:
        if items in letters_guessed:
            new = new + items
        else:
            new = new + '_'
    return new


def GetWordSeparatedBySpaces(word):
    new = ''
    for i in range(0, len(word) -1):
        new = new + word[i] + " "
    return new +  word[-1]
        

def IsWinner(answer, letters_guessed):
    pass
    count = 0
    for letters in answer:
        if letters in letters_guessed:
            count = count + 1
    return count == len(answer)


def IsLegalGuess(current_guess, letters_guessed):
    pass
    if current_guess.isalpha() and len(current_guess) == 1:
        if current_guess not in letters_guessed:
            return True
    return False



def GetLegalGuess(letters_guessed):
  
    while True:
        get_letter = input("Please enter your guess letter: ")
        if IsLegalGuess(get_letter, letters_guessed):
            return get_letter



def IsGuessRevealing(answer, legal_letter_guess):
    for items in answer:
        if items == legal_letter_guess:
            return True
    return False


def GetAllEnglishWords():
    get_words = open("hangman_english_words.txt", 'r')
    words_list = []
    for line in get_words:
        line = line.rstrip()
        words_list.append(line)
    return words_list


answer = GetAllEnglishWords()
if answer != None and 'voting' in answer:
    text = 'PASS'
else:
    text = 'FAIL'
print('GetAllEnglishWords #1: expected the word voting', text)
if answer != None and 'triage' not in answer:
    text = 'PASS'
else:
    text = 'FAIL'
print('GetAllEnglishWords #2: did not expect triage', text)


import random
def GetRandomWord(words):
    return random.choice(words)





def Play(answer):
    strike = 5
    letters_guessed = ''
    while strike > 0:
        print (GetWordSeparatedBySpaces(GetAnswerWithUnderscores(answer, letters_guessed)))
        guess_letter = input("Guess: ")
        guess_letter = guess_letter.upper()
        if IsWinner(answer, letters_guessed):
            print ('You have won')
            break
        if IsLegalGuess(guess_letter, letters_guessed) and IsGuessRevealing(answer, guess_letter):
            print ('Good guess! Continue')
            letters_guessed = letters_guessed + guess_letter
            if IsWinner(answer, letters_guessed):
                print ('You have won')
                break
            else:
                continue
        elif guess_letter in letters_guessed:
            print ('Oops, You have already guessed letter ' + guess_letter)
        else:
            strike = strike - 1
            print (guess_letter + ' is not in the word. You have ' + str(strike) +  ' strikes.')
    if strike == 0:
        print ('You have lost. The answer is' + answer)

    
import random
def StartupAndPlay():
    words_list = GetAllEnglishWords()
    while True:
        answer = random.choice(words_list).upper()
        print answer
        Play(answer)

        prompt = raw_input('Do you want to play again? If yes, type \'yes\' or \'Yes\' Else: type \'No\' ')
        if prompt.lower() != 'yes':
            break

        
def GetPlayRecord():
    open_file = open('hangman_play_record.txt', 'r')
    read_file = open_file.read()
    split_file = read_file.split(',')
    game_record = [int(num) for num in split_file]
    return game_record




def Play1(answer):
    strike = 5
    letters_guessed = ''
    while strike > 0:
        print (GetWordSeparatedBySpaces(GetAnswerWithUnderscores(answer, letters_guessed)))
        guess_letter = raw_input("Guess: ")
        guess_letter = guess_letter.upper()
        if IsWinner(answer, letters_guessed):
            print ('You have won')
            break
        if IsLegalGuess(guess_letter, letters_guessed) and IsGuessRevealing(answer, guess_letter):
            print ('Good guess! Continue')
            letters_guessed = letters_guessed + guess_letter
            if IsWinner(answer, letters_guessed):
                print ('You have won')
                break
            else:
                continue
        elif guess_letter in letters_guessed:
            print ('Oops, You have already guessed letter ' + guess_letter)
        else:
            strike = strike - 1
            print (guess_letter + ' is not in the word. You have ' + str(strike) +  ' strikes.')
    if strike == 0:
        print ('You have lost')
    RecordPlay(IsWinner(answer, letters_guessed))


'''-----------------------------------------------------------
Extra credit exercise 2:
Write a function that records whether the user played and won or
lost in the 'hangman_play_record.txt' file. The parameter should
be a boolean type, where True signifies a win and False signifies
a loss. Read Extra credit exercise 1 for information about the 
format of the 'hangman_play_record.txt' file.
'''
def RecordPlay(win):
    get_play_record = GetPlayRecord()
    get_play_record[0] += 1
    if win:
        get_play_record[1] += 1
    get_file = open('hangman_play_record.txt', 'w')
    get_file.write(str(get_play_record[0])+ ',' + str(get_play_record[1]))
    


'''-----------------------------------------------------------
Extra credit exercise 3:
This function should be an expansion of StartupAndPlay. NOTE: even
if you do this bonus exercise, leave your StartupAndPlay function
as is!

First, copy all of the code you wrote for StartupAndPlay into this
new function. Add in the following:
* Code that makes use of GetPlayRecord and RecordPlay.
* When playing Hangman for the first time, display how many times
  the user win, and how many games they've played
* Each time the user wins or loses a single play of Hangman,
  display their new number of wins and total games played.
'''
def StartupAndPlayVersion2():
    words_list = GetAllEnglishWords()
    while True:
        print ('Number of Time Played : ' + str(GetPlayRecord()[0]))
        print ('Number of Time Won : ' + str(GetPlayRecord()[1]))
        answer = random.choice(words_list).upper()
        Play1(answer)
        print ('Number of Time Played : ' + str(GetPlayRecord()[0]))
        print ('Number of Time Won : ' + str(GetPlayRecord()[1]))

        prompt = raw_input('Do you want to play again? If yes, type \'yes\' or \'Yes\' Else: type \'No\' ')
        if prompt.lower() != 'yes':
            break



'''-----------------------------------------------------------
Extra credit exercise 4:
1. Copy the code you wrote for Exercise 6 and paste it here, but
   instead of calling StartupAndPlay, call StartupAndPlayVersion2.
   DO NOT change your answer for Exercise 6!
2. Comment out the code you wrote for Exercise 6. Again, DO NOT
   delete the code you wrote for Exercise 6!
'''
if __name__ == '__main__':
    StartupAndPlayVersion2()
