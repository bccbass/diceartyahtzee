from pyfiglet import Figlet
import dice_bctweak
import dice_art 
from colorama import Fore
f = Figlet(font='slant', justify='center')

print(Fore.CYAN + f.renderText('Yahtzee'))

dice_art.print_hand([1,2,3,4,5,6])
# dice_bctweak.print_hand([1,2,3,4,5,6])
