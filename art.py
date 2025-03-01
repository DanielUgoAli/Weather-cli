try:
    import pyfiglet # type: ignore
    has_pyfiglet = True
except ImportError:
    has_pyfiglet = False


def print_art(text, font='standard'):
    if has_pyfiglet:
        if font == 'standard':
            art = pyfiglet.figlet_format(text)
        else:
            art = pyfiglet.figlet_format(text, font=font)
        print(art)
    else:
        print("Please install the pyfiglet library to use this feature")
        print("pip install pyfiglet")
        print("Or you can use the 'art' command in the terminal to generate ascii art")
