secret = 38

while True:
    try:
        guess = int(input("Guess the secret number: "))

        if guess > 10000:
            print("Go smaller!")
        #type(guess) != int:
            #print("It has to be a number, you know!")
       # elif type(guess) == float:
           # print("No decimal numbers.")
        elif guess > 1000:
            print("It's waaaay lower!")
        elif guess > 100:
            print("It's a two digit number wink wink.")
        elif guess < 10:
            print("It's a two digit number wink wink.")
        elif guess > 29 and guess < 40 and guess != 38:
            print("YOU'RE ALMOST THERE!")
        elif guess <= 50 and guess > 9 and guess != secret:
            print("Getting warmer...")
        elif guess >= 50 and guess < 100 and guess != secret:
            print("Hmmm, not quite.")
        elif guess == secret:
            print("Woooo, you got it! Here's a metaphysical cookie!")
            break
        else:
            none
    except ValueError:
        print("It has to be an integer, you know!")