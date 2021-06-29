import random

name = input("Enter Your User-Name: ")
print("Good Luck ",name)
allowed_error = 7
words = ['programming','computer','machine','laptop','fruit','increase','partial','positive','negetive',"january","border","image","film","promise","kids","lungs","doll","rhyme","damage","plants"]
word  = random.choice(words)
guesses = []
done = False

while not done:
    for letter in word:
        if letter.lower() in guesses:
            print(letter,end=' ')
        else:
            print('_',end=' ')
    
    print("")
    guess_letter = str(input(f"Allowed error {allowed_error}, Enter your Guessing Letter: "))
    guesses.append(guess_letter.lower())
    if guess_letter.lower() not in word.lower():
        allowed_error -= 1
    
    if allowed_error == 0:
        break 
    done = True
    for letter in word:
        if letter.lower() not in guesses:
            done = False
    
if done:
    print("You Found the Word: {}".format(word))
else:
    print("Game Over. Better Luck next time.")
