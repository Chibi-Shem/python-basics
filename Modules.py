import Tkinter
import tkMessageBox
from geopy.geocoders import Nominatim
import math
import BasicSyntax

main = Tkinter.Tk()
main.withdraw()

print(tkMessageBox.showinfo('a title', 'hi'))
location = Nominatim().geocode('Digos')
print(location.address)

print(dir(__builtins__))
print(math.exp(5))
print(math.log10(5))
print(math.pow(5, 2))
print(math.sqrt(25))
print(globals().keys())


def print_local_vars():
    """Prints all local variables."""
    x = 'i am local'
    print(locals().values())


print_local_vars()
