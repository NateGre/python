import random

#initalize while loop
usr_prompt = 'Y'
#create dictionary of totals with empty values
total_sums = {
                "2":'', "3":'',
                "4":'', "5":'',
                "6":'', "7":'',
                "8":'', "9":'',
                "10":'', "11":'',
                "12":''
             }


#adds the string '*' to the corresponding key in the total_sums dict
#ex. if roll_total = 6 is rolled twice the value for total_sums["6"] is '**'
while usr_prompt == 'Y':
    num_rolls = int(input('Enter number of rolls:\n'))
    if num_rolls >= 1:
        for i in range(num_rolls):
            die1 = random.randint(1,6)
            die2 = random.randint(1,6)
            roll_total = die1 + die2

            if roll_total == 2:
                total_sums["2"] = '*' + total_sums["2"]
            if roll_total == 3:
                total_sums["3"] = '*' + total_sums["3"]
            if roll_total == 4:
                total_sums["4"] = '*' + total_sums["4"]
            if roll_total == 5:
                total_sums["5"] = '*' + total_sums["5"]
            if roll_total == 6:
                total_sums["6"] = '*' + total_sums["6"]
            if roll_total == 7:
                total_sums["7"] = '*' + total_sums["7"]
            if roll_total == 8:
                total_sums["8"] = '*' + total_sums["8"]
            if roll_total == 9:
                total_sums["9"] = '*' + total_sums["9"]
            if roll_total == 10:
                total_sums["10"] = '*' + total_sums["10"]
            if roll_total == 11:
                total_sums["11"] = '*' + total_sums["11"]
            if roll_total == 12:
                total_sums["12"] = '*' + total_sums["12"]       
    else:
        print('Invalid number of rolls. Try again.')

#print results
    print('\nDice roll statistics:')
    print('2s:', total_sums["2"])
    print('3s:', total_sums["3"])
    print('4s:', total_sums["4"])
    print('5s:', total_sums["5"])
    print('6s:', total_sums["6"])
    print('7s:', total_sums["7"])
    print('8s:', total_sums["8"])
    print('9s:', total_sums["9"])
    print('10s:', total_sums["10"])
    print('11s:', total_sums["11"])
    print('12s:', total_sums["12"])

#ask user if they want to continue
    usr_prompt = input('Continue? Y or N:')
    if usr_prompt == 'N':
        exit()
#if user answered 'Y' ask if they want to reset values inside of total_sums
    reset_stats = input('Reset stats? Y or N:')
    if reset_stats == 'Y':
        total_sums = {
                "2":'', "3":'',
                "4":'', "5":'',
                "6":'', "7":'',
                "8":'', "9":'',
                "10":'', "11":'',
                "12":''
             }
        continue
        

