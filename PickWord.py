import random
import turtle

drawHang = turtle.Turtle() #global turtle to draw game

def get_word(): # function that pulls a random word from txt file
    a = random.randint(1, 10) # choose a random number to find random word
    a1 = str(a)
    word = "" # set a string to hold the word

    with open("C:\\Users\\kyle\\Desktop\\Hangman.txt", "r") as f: # open the file
        for i, line in enumerate(f): # go through the txt file and read words
            if i == a: # if the line
                word = line.strip() # remove any spaces
                print(line) # print string for debug
        f.close() # close files
        return word # return word

def find_index(index): # find the index of the letters in the word
    inword = False
    for x in hangman_copy: # go through the word and check letters
        if x == letter: # if the letter the user guessed is in the word
            letter_locations.append(index)  # add that location to the location list
            inword = True
        index = index + 1 # move index to check next letter
    return letter_locations, inword # return letter locations and if it is not in word

def draw_hangman(draw):

    if draw == "lost":
        lostGame()
        turtle.done()
    if draw == "head":
        turtle.shape("circle")
        turtle.shapesize(5, 5)
    if draw == "body":
        drawHang.penup()
        drawHang.home()
        drawHang.pendown()
        drawHang.right(90)
        drawHang.forward(200)
    if draw == "rightLeg":
        drawHang.penup()
        drawHang.home()
        drawHang.right(90)
        drawHang.forward(200)
        drawHang.pendown()
        drawHang.right(45)
        drawHang.forward(75)
    if draw == "leftLeg":
        drawHang.penup()
        drawHang.home()
        drawHang.right(90)
        drawHang.forward(200)
        drawHang.pendown()
        drawHang.left(45)
        drawHang.forward(75)
    if draw == "armOne":
        drawHang.penup()
        drawHang.home()
        drawHang.right(90)
        drawHang.forward(100)
        drawHang.pendown()
        drawHang.left(45)
        drawHang.forward(75)
    if draw == "armTwo":
        drawHang.penup()
        drawHang.home()
        drawHang.right(90)
        drawHang.forward(100)
        drawHang.pendown()
        drawHang.right(45)
        drawHang.forward(75)


def lostGame():
    print("You did not save the hangman")


def hangingPlatform():
    drawHang.left(90)
    drawHang.forward(50)
    drawHang.left(90)
    drawHang.forward(100)
    drawHang.left(90)
    drawHang.forward(300)
    drawHang.left(90)
    drawHang.forward(75)
    drawHang.backward(150)



print("Lets play Hangman")

hangingPlatform()

guesses = 1 # set number of guesses start at 1 because it is smallest amount
letter_locations = [] # set a list that will hold the letter loctions
hangman_list = []
bodyParts = ["head","body","rightLeg","leftLeg","armOne","armTwo","lost"]
numWrong = 0

index = 0
word = get_word()

hangman = list(word) # break the word into a list by char
hangman_copy = list(word) # break the word into a second list that will be shown to user

for x in hangman:
    hangman_list.append("_") # change the values in the list to be shown to user to _ to hide values but keep size


letter = input("Guess a letter\n") # ask the user to guess a letter

letter_locations, inword = find_index(index)

if inword == False: # checks if the letter was found in the word
    print("That letter is not in the word")
    draw_hangman(bodyParts[numWrong])
    numWrong += 1 # count number wrong to iterate through drawing array
if inword == True:
    print("Congratz you guessed a letter")

for x in letter_locations:
   hangman_list[x] = letter
print(hangman_list)

for i in hangman_copy:
    if letter == i:
        hangman = [elem for elem in hangman if elem != letter] # remove correct letters guessed from hangman list
letter_locations = []

while len(hangman) != 0: # while the list is not empty keep asking user for input
    letter = input("Guess Again\n")
    letter_locations , inword = find_index(index)
    if inword == False:
        print("That letter is not in the word")
        draw_hangman(bodyParts[numWrong])
        numWrong += 1
    for x in letter_locations:
        hangman_list[x] = letter
    print(hangman_list)
    for i in hangman_copy:
        if letter == i:
            hangman = [elem for elem in hangman if elem != letter]
            print(hangman)
    guesses = guesses + 1
    index = 0
    letter_locations = []


print("Congratz")
print("It took you " + str(guesses) + " guesses")
