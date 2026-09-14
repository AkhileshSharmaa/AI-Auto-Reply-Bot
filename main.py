import time

from chat_module import create_reply
from mouse_module import open_browser


def main():

    print("=" * 60)
    print("AI AUTO BOT REPLY")
    print("=" * 60)

    print("\nOpening browser...")

    open_browser()

    print("\nStarting chat monitoring...")

    time.sleep(3)

    while True:

        try:

            reply = create_reply()

            if reply:

                print("\nReply sent successfully.")

            else:

                print("\nNo reply generated.")

            time.sleep(10)

        except KeyboardInterrupt:

            print("\nStopping bot...")

            break

        except Exception as e:

            print("\nError:", e)

            time.sleep(3)

if __name__ == "__main__":
    main()