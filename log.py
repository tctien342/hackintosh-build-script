def c(text, color):
    # colored output https://stackoverflow.com/a/56774969
    return "\33[38;5;{}m{}\33[0m".format(color, text)


PREFIX_INFO = c('<i>', 75)
PREFIX_ADD = c('<+>', 12)
PREFIX_ERR = c('<e>', 9)
ARROW = c('==>', 40)


def title(*args):
    print(PREFIX_INFO, *args)


def sub(*args):
    print(PREFIX_ADD, *args)


def prompt(msg: str, bypass: bool = False):
    if bypass:
        return ''
    return input(ARROW + ' ' + msg)


def confirm(msg: str, bypass: bool = False) -> bool:
    if bypass:
        return True
    r = prompt(msg + '?(Y/n)')
    return r != 'n'
