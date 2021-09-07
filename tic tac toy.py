dict = { '1' : ' ', '2' : ' ', '3' : ' ', '4' : ' ', '5' : ' ', '6' : ' ', '7' : ' ', '8' : ' ', '9' : ' ' }

#print('1|2|3\n-+-+-\n4|5|6\n-+-+-\n7|8|9')

player = 1
moves = 0
check = 0

def check():
    #horizontal
    if dict['1'] == 'X' and dict['2'] == 'X' and dict['3'] == 'X':
        print('Player 1 won!')
        return 1
    if dict['4'] == 'X' and dict['5'] == 'X' and dict['6'] == 'X':
        print('Player 1 won!')
        return 1
    if dict['7'] == 'X' and dict['8'] == 'X' and dict['9'] == 'X':
        print('Player 1 won!')
        return 1
    if dict['1'] == 'O' and dict['2'] == 'O' and dict['3'] == 'O':
        print('Player 2 won!')
        return 1
    if dict['4'] == 'O' and dict['5'] == 'O' and dict['6'] == 'O':
        print('Player 2 won!')
        return 1
    if dict['7'] == 'O' and dict['8'] == 'O' and dict['9'] == 'O':
        print('Player 2 won!')
        return 1
    #vertical
    if dict['1'] == 'X' and dict['4'] == 'X' and dict['7'] == 'X':
        print('Player 1 won!')
        return 1
    if dict['2'] == 'X' and dict['5'] == 'X' and dict['8'] == 'X':
        print('Player 1 won!')
        return 1
    if dict['3'] == 'X' and dict['6'] == 'X' and dict['9'] == 'X':
        print('Player 1 won!')
        return 1
    if dict['1'] == 'O' and dict['4'] == 'O' and dict['7'] == 'O':
        print('Player 2 won!')
        return 1
    if dict['2'] == 'O' and dict['5'] == 'O' and dict['8'] == 'O':
        print('Player 2 won!')
        return 1
    if dict['3'] == 'O' and dict['6'] == 'O' and dict['9'] == 'O':
        print('Player 2 won!')
        return 1
    #diagonal
    if dict['1'] == 'X' and dict['5'] == 'X' and dict['9'] == 'X':
        print('Player 1 won!')
        return 1
    if dict['3'] == 'X' and dict['5'] == 'X' and dict['7'] == 'X':
        print('Player 1 won!')
        return 1
    if dict['1'] == 'O' and dict['5'] == 'O' and dict['9'] == 'O':
        print('Player 2 won!')
        return 1
    if dict['3'] == 'O' and dict['5'] == 'O' and dict['7'] == 'O':
        print('Player 2 won!')
        return 1
    return 0



while True:
    print(dict['1']+'|'+dict['2']+'|'+dict['3'])
    print('-+-+-')
    print(dict['4']+'|'+dict['5']+'|'+dict['6'])
    print('-+-+-')
    print(dict['7']+'|'+dict['8']+'|'+dict['9'])
    end_check = check()
    if moves == 9 or end_check == 1:
        break
    while True:
        if player == 1:
         input1 = input('position for player 1')
         if input1 in dict and dict[input1] == ' ':
             dict[input1] = 'X'
             player = 2
             break
         else:
             print('Invalid Input')
             continue
        else:
            input2 = input('position for player 2')
            if input2 in dict and dict[input2] == ' ':
                dict[input2] = 'O'
                player = 1
                break
            else:
                print('Invalid Input')
                continue
moves += 1
print('*************************')

