import pyperclip
import time


def copy_from_clipboard():
    """
    Returns the current text stored in the clipboard.
    """

    time.sleep(0.5)

    return pyperclip.paste()


def copy_to_clipboard(text):
    """
    Copies text to the clipboard.
    """

    pyperclip.copy(text)