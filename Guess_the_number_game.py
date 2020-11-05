n=10
mynumber = 77
print("This is a guess game")
print("guesses left are:", n)
while (n<=10 and n>0):
    n = n - 1
    number = int(input("Enter number between 1-100"))
    if number < mynumber:
        print("Guess greater\nGuesses left are:", n)
    elif number > mynumber:
        print("Guess lesser\nGuesses left are:", n)
    elif number == mynumber:
        print("Congrats your guess is correct and no. of Guesses you took is", 10-n)
        break
if n==0:
    print("game over")