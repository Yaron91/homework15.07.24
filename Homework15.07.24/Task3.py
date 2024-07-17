# Part 1 - get a positive number from the user and symmetrical print it
user_num: int = int (input("Please enter a number bigger than 0: "));

for j in range (1, user_num+1):
    for i in range (1, j+1):
        print (i, end=" ")
    print()
for j in range (user_num -1, 0, -1):
    for i in range (1, j+1):
        print (i, end=" ")
    print()


# Part 2 - get a positive number from the user and symmetrical print * equal to the user's number

user_num2: int = int (input("Please enter a number bigger than 0: "));
while True:
    if user_num2 % 2 ==0:
        print ("Please enter only odd numbers" );
        user_num2: int = int(input("Please enter a number bigger than 0: "));
    else:
        break

for j in range (user_num2):
    for i in range (user_num2 - j -1):
        print(" ", end="")
    for j in range ( 2 * j + 1):
        print ("*", end="")
    print()
