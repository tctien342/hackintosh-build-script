def c(text, color):
    """Out put an colored text

    Args:
        text (str): content that need to be colored
        color (int): index of color can be found in https://stackoverflow.com/a/56774969

    Returns:
        str: colored text in terminal
    """
    return "\33[38;5;{}m{}\33[0m".format(color, text)


PREFIX_INFO = c('<i>', 75)
PREFIX_ADD = c('<+>', 12)
PREFIX_ERR = c('<e>', 9)
ARROW = c('==>', 40)


def title(*args):
    """Print an title
    """
    print(PREFIX_INFO, *args)


def sub(*args):
    """Print an subtitle content
    """
    print(PREFIX_ADD, *args)


def prompt(msg: str, bypass: bool = False):
    """Ask user something

    Args:
        msg (str): content of question
        bypass (bool, optional): bypass question if set to True. Defaults to False.

    Returns:
        str: answer of user
    """
    if bypass:
        return ''
    return input(ARROW + ' ' + msg)


def confirm(msg: str, bypass: bool = False) -> bool:
    """Ask user with yes no question

    Args:
        msg (str): content of question
        bypass (bool, optional): bypass question an auto return True. Defaults to False.

    Returns:
        bool: answer of user
    """
    if bypass:
        return True
    r = prompt(msg + '?(Y/n)')
    return r != 'n'
