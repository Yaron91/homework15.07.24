number: int = 0
positive_numbers: int = 0
negative_numbers: int = 0
neutral_number: int = 0
divide_7: int = 0
last_positive: int= None
last_negative: int = None

for i in range (1,11):
    number= int (input ("Please enter any number: "));
    if number == -9999:
        break
    else:
        if number < -1000 or number > 1000:
            continue
        if number %7 == 0 :
            divide_7 += 1
        if number > 0 :
            positive_numbers += 1
            last_positive = number
        if number < 0 :
            negative_numbers += 1
            last_negative = number
        if number == 0 :
            neutral_number += 1
print (f"The number of numbers bigger than 0 are {positive_numbers}" );
print (f"The number of numbers lower than 0 are {negative_numbers}" );
print (f"The number of numbers equal to 0 are {neutral_number}" );
print (f"The number of numbers divided by 7 are {divide_7}" );
print (f" The last positive number entered was {last_positive}");
print(f" The last negative number entered was {last_negative}");

