from marq_counter import MarqueeCounter

lettersArray = ['$', '-', '.', '&', '0', '1', '2', '3', '4', '5',
                '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F',
                'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
                'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# list of all possible char
num_of_letters = []  # the AMOUNT of ALL letters in 'Current'
new_num_of_letters = []  # the AMOUNT of ALL letters in 'New'
needed = []  # a list that stores the AMOUNT of ONLY the 'needed' letters
new_lettersArray = []  # list of just the CHARs needed
counterObj = MarqueeCounter()

doubleSided = counterObj.yes_or_no(input('Is this a double sided change?').lower())

if doubleSided is False:
    SIDE_A = input("What is currently on the marquee?\n")
    NEW_SIDE_A = input("What needs to go up?\n")

    print('\n\nCurrent - {}\n\nNew - {}\n\n'.format(SIDE_A.upper(), NEW_SIDE_A.upper()))

    num_letters_SIDE_A = counterObj.count_all_letters(SIDE_A)
    NEW_num_letters_SIDE_A = counterObj.count_all_letters(NEW_SIDE_A)

    total_needed, newLetters = counterObj.needed_letters(NEW_num_letters_SIDE_A, num_letters_SIDE_A)

    counterObj.printing_whats_needed(total_needed, newLetters)

else:

    SIDE_A = input("What is on SIDE A?\n")
    SIDE_B = input("What is on SIDE B?\n")
    NEW_SIDE_A = input("Enter First new side\n")
    NEW_SIDE_B = input("Enter Second new side\n")

    print(
        '\n\nSIDE A-{}\nSIDE B-{}\n\nFirst New-{}\nSecond New-{}\n\n'.format(SIDE_A.upper(), SIDE_B.upper(),
                                                                             NEW_SIDE_A.upper(), NEW_SIDE_B.upper()))

    total_Num_letters = counterObj.count_all_letters(SIDE_A + SIDE_B)
    NEW_total_Num_letters = counterObj.count_all_letters("{0}{1}".format(NEW_SIDE_A, NEW_SIDE_B))

    total_needed, newLetters = counterObj.needed_letters(NEW_total_Num_letters, total_Num_letters)

    counterObj.printing_whats_needed(total_needed, newLetters)
