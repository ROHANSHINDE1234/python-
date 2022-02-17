# guess the number
# no of guesses available
# print number of guess left
# no of guess he took to finish

n = 22
print('"In this game you have to guess a particular number \n which is predefined" \n "No of guesses you have = 7"')
guess_no = int(input("Enter your guessed number: "))
no_of_guess = 6
a = no_of_guess

for i in range(no_of_guess+1):
    d = a-i
    if d!=0:

        if guess_no > n:
            print('"The guessed number is bigger than the number you have to guess"')
            print("no of guesses left ", d)
            guess_no = int(input("Try again: "))



        elif guess_no < n:
            print('"The guessed number is smaller than the number you have to guess"')
            print("no of guess left", d)
            guess_no = int(input("Try again: "))


        elif guess_no == n:
            print("You guessed the right number")
            print("You guessed in", i+1 ,"Guess")
            break

    else:
        print("You loose no guess left")
        print("You lost")