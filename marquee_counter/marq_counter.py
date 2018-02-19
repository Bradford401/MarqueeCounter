class MarqueeCounter:

    @staticmethod
    def count_all_letters(current_string: object):
        letters_array = ['$', '-', '.', '&', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A',
                         'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
                         'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        num_of_letters_a = []
        for x in range(0, 40):
            num_of_letters_a.append(current_string.upper().count(letters_array[x]))
        return num_of_letters_a

    @staticmethod
    def needed_letters(new_num, current_num):
        letters_array = ['$', '-', '.', '&', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A',
                         'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
                         'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        total_needed = []
        new_letters = []
        for x in range(0, 40):
            if new_num[x] > current_num[x]:
                total_needed.append((new_num[x] - current_num[x]))
                new_letters.append(letters_array[x])
        return total_needed, new_letters

    @staticmethod
    def printing_whats_needed(needed, new_letters):
        needed_len = len(needed)
        if needed_len == 0:
            print('No extra letters needed')
        for x in range(0, needed_len):
            print("{} needed for {}".format(needed[x], new_letters[x]))

    @staticmethod
    def yes_or_no(answer):
        yes = {'yes', 'y', 'ye', ''}
        no = {'no', 'n', 'nope'}
        x = 0
        while x == 0:
            if answer in yes:
                x += 1
                return True
            elif answer in no:
                x += 1
                return False
            else:
                print("Please respond with 'yes' or 'no'")
