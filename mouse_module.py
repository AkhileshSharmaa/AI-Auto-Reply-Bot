import pyautogui
import time

BROWSER_ICON = (373, 246)

CHAT_START = (535, 1252

CHAT_END = (648, 882)

MESSAGE_BOX = (386, 416)


def open_browser():

    print("Opening browser...")

    pyautogui.click(*BROWSER_ICON)

    time.sleep(3)

    print("Browser opened.")


def select_chat():

    print("Selecting chat...")

    pyautogui.moveTo(*CHAT_START)

    pyautogui.dragTo(
        *CHAT_END,
        duration=2.0,
        button="left"
    )

    time.sleep(0.5)

def copy_chat():

    print("Copying chat...")

    pyautogui.hotkey("ctrl", "c")

    time.sleep(1)

def click_message_box():

    print("Clicking message box...")

    pyautogui.click(*MESSAGE_BOX)

    time.sleep(0.5)


def paste_message():

    print("Pasting reply...")

    pyautogui.hotkey("ctrl", "v")

    time.sleep(0.5)


def send_message():

    print("Sending message...")

    pyautogui.press("enter")

    time.sleep(1)
