import random

while True:
    rnd_num: int = random.randint (1, 101)
    count: int = 0

    while True:
        user_num: int = int (input (" Please enter any number between 1-100: "));
        if user_num == rnd_num:
            count += 1
            print( "Bingo!")
            break
        elif user_num > rnd_num:
            count += 1
            print ("Your number is too big ");
            continue
        elif user_num < rnd_num:
            count += 1
            print("Your number is too small ");
    print (f"The number of tries were {count} ");

    play_again: str = input("Would you like to play again (yes/no)? ") .lower()
    if play_again != 'yes':
        print ("Thank you for playing!");
        break

