#checklist
#double charater
# past charater

import time
import random
hngmn = ['''
             
                +---+
                |   |
                    |
                    |
                    |
                    |
              =========''', '''
             
                +---+
                |   |
                O   |
                    |
                    |
                    |
              =========''', '''
             
                +---+
                |   |
                O   |
                |   |
                    |
                    |
              =========''', '''
             
                +---+
                |   |
                O   |
               /|   |
                    |
                    |
              =========''', '''
             
                +---+
                |   |
                O   |
               /|\  |
                    |
                    |
              =========''', '''
             
                +---+
                |   |
                O   |
               /|\  |
               /    |
                    |
              =========''', '''
                +---+
                |   |
                O   |
               /|\  |
               / \  |
                    |
              =========''']

hanged_man = '''
                +---+
                |   |
               _O_  |
                |   |
               / \  |
                    |
              ========='''

free_man = ['''
                +---+
                    |
                    |
               _O_  |
                |   |
               | |  |
              =========''','''
                +---+
                    |
                    |
               \O/  |
                |   |
               | |  |
              =========''']

def word_list():
    words = open("words.txt", "r")
    word_list = []
    for line in words: #repeats for as many lines in the text file
        stripped_line = line.strip() #strips all the words from a line making it a list
        line_list = stripped_line.split() 
        word_list.append(line_list)
    words.close() 
    return word_list #returns a list full of words


def check_letter(letter, word, outline, letters_in):
    true = False
    i = 0
    for w in word:
        if letter == w:
            outline = outline[0:(i*3)+1]+letter+outline[(i*3)+2:]
            print(outline)
            true = True     
        i += 1
    return true, outline   

def shadow(word):
    return (f" _ "*len(word))

def error_check(letter, used_letters):      
    if isinstance(letter, str) == False or len(letter) != 1:
        print("invalid user input")  
        return False
    for i in used_letters:
        if i == letter:
            print("Used as a past letter please enter again")
            return False
    return True
def main():
    clear = f"\n\n\n\n\n\n"*9
    print(clear,"Welcome to hangman: ")
    while True:
        print(clear, hngmn[0])
        used_letters = []
        word = "".join(random.choice(word_list()))
        word = word.lower()
        letters_in = [word[i] for i in range(len(word))]
        outline = shadow(word)
        stage = 1
        while True:
            print("Used Letters: ", used_letters)
            print(outline)
            while True:
                letter = input("Please input a letter: ").lower()
                if error_check(letter, used_letters) == True:
                    break
            check, outline = check_letter(letter, word, outline, letters_in)  
            if word == outline.replace("_", "").replace(" ", ""):           
                for i in range(4):
                    print(clear,free_man[0])
                    time.sleep(1)
                    print(clear, free_man[1])
                    time.sleep(1)
                break
            if check == True: 
                print(hngmn[stage-1])    
            else:
                print(hngmn[stage-1])
                stage += 1
            if stage == 7:
                print(clear,hanged_man)
                print(f"You lost! The word was {word}.")
                time.sleep(4)
                break
            used_letters += letter
            print(outline)


if __name__ == "__main__":
    main()