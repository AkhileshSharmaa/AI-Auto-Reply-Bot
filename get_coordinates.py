import pyautogui
import time

print("=" * 50)
print("MOUSE COORDINATE FINDER")
print("=" * 50)

print("\nMove your mouse to the location you want.")
print("The coordinates will update every 0.5 seconds.")
print("Press Ctrl+C to stop.\n")

try:
    while True:

        x, y = pyautogui.position()

        print(f"X = {x:4}   Y = {y:4}", end="\r")
        time.sleep(0.5)

except KeyboardInterrupt:

    print("\n\nCoordinate finder stopped.")