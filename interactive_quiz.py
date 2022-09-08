def interactive():
    one = '1.are you human?\nA.yes\nB.no\nC.maybe\t'
    two = '2.do you like girls?\nA.a lot\nB.hell no\nC.sometimes\t'
    three = "3.how is your cit course going?\nA.really well\nB.I'm behind \nC.I'll get there\t"
    questions = [one,two,three]
    points = 0
    for q in questions:
        choice = input(q)
        if q == one and choice.upper() == 'A':
            points += 5
            print(f"correct. well done!")
        elif q == two and choice.upper() == 'B':
            points += 5
            print(f"correct. well done!\n") 
        elif q == three and choice.upper() == 'C':
                points += 5
                print(f"{choice} is correct. well done!\n")
        else:
            print(f"{choice} is wrong,try again\n")
    print(f'your total score is {points} out of 15 ')
interactive()