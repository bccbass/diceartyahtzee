import colorama
from colorama import Fore, Back, Style

colorama.init()




dice_art = {
1: (
'┌─────────┐',
'│         │',
'│    ●    │',
'│         │',
'└─────────┘'
),
2: (
'┌─────────┐',
'│  ●      │',
'│         │',
'│      ●  │',
'└─────────┘'
),
3: (
'┌─────────┐',
'│ ●       │',
'│    ●    │',
'│       ● │',
'└─────────┘'
),
4: (
'┌─────────┐',
'│  ●   ●  │',
'│         │',
'│  ●   ●  │',
'└─────────┘'
),
5: (
'┌─────────┐',
'│ ●     ● │',
'│    ●    │',
'│ ●     ● │',
'└─────────┘'
),
6: (
'┌─────────┐',
'│  ●   ●  │',
'│  ●   ●  │',
'│  ●   ●  │',
'└─────────┘'
),
}

color = (
'BLUE',
'GREEN',
'RED',
'CYAN',
'BLACK',
'MAGENTA',
)

def print_hand(hand):
    for i in range(5):
        for die in hand:
            if die % 2 == 0: 
                print(Fore.YELLOW + dice_art[die][i], end=Fore.RESET+'   ')
            else:
                print(Fore.WHITE+ dice_art[die][i], end=Fore.RESET+'   ') 
            # print(dice_art[die][i], end='')
        print(' ')
    print(Fore.RESET)
            

