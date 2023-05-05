import colorama
from colorama import Fore, Back, Style

colorama.init()




dice_art = {
1: (
'       ',
'   ●   ',
'       ',
),
2: (
' ●     ',
'       ',
'     ● ',
),
3: (
' ●     ',
'   ●   ',
'     ● ',
),
4: (
' ●   ● ',
'       ',
' ●   ● ',
),
5: (
' ●   ● ',
'   ●   ',
' ●   ● ',
),
6: (
' ●   ● ',
' ●   ● ',
' ●   ● ',
),
}



def print_hand(hand):
    for i in range(3):
        for die in hand:
            if die % 2 == 0: 
                print(Fore.BLUE + Back.WHITE + dice_art[die][i], end=Back.RESET+'   ')
            else:
                print(Fore.WHITE+ Back.BLUE + dice_art[die][i], end=Back.RESET+'   ') 
            # print(dice_art[die][i], end='')
        print(' ')
    print(Fore.RESET)
            


# print_hand([1,2,3,4,5,6])
# print('hi')
