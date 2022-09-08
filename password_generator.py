from random import seed
from random import randint
from string import punctuation,ascii_lowercase,ascii_uppercase,digits
# seed random number generator
# seed(0)
def passwordGen(length):
    length = input("enter length of password:")
    char_tuple = tuple(punctuation)
    lower_tuple = tuple(ascii_lowercase)
    upper_tuple = tuple(ascii_uppercase)
    digit_tuple = tuple(digits)
    password_list = list()
    if int(length) >= 6: 
        for num in range(int(length)):
            value = randint(1,4)
            if value== 1 :
                char_tuple_index = randint(0,32)
                password_list.append(char_tuple[char_tuple_index-1])

            elif  value== 2:
                lower_tuple_index = randint(0,26)
                password_list.append(lower_tuple[lower_tuple_index-1])
            elif  value== 3 :
                upper_tuple_index = randint(0,26)
                password_list.append(upper_tuple[upper_tuple_index-1])
            elif  value== 4:
                digit_tuple_index = randint(0,9)
                password_list.append(digit_tuple[digit_tuple_index-1])
        value = 0
        # password_list.reverse()
        password_string = ''.join(str(e) for e in password_list)
        return password_string
    else:
        print("cant generate for less than 6 characters")    
print(passwordGen(8))