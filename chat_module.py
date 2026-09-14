from clipboard_module import (
    copy_from_clipboard,
    copy_to_clipboard
)

from gemini_module import generate_reply

from mouse_module import (
    select_chat,
    copy_chat,
    click_message_box,
    paste_message,
    send_message
)

def get_chat_history():

    # Select chat
    select_chat()

    # Copy selected text
    copy_chat()

    # Read clipboard
    chat_history = copy_from_clipboard()

    return chat_history


def create_reply():

    chat_history = get_chat_history()

    if not chat_history.strip():

        print("\nNo chat text found.")

        return None

    print("\n" + "=" * 60)
    print("CHAT HISTORY")
    print("=" * 60)

    print(chat_history)

    print("\n" + "=" * 60)
    print("ASKING GEMINI...")
    print("=" * 60)

    reply = generate_reply(chat_history)

    if not reply:

        print("\nGemini did not generate a reply.")

        return None

    print("\n" + "=" * 60)
    print("GENERATED REPLY")
    print("=" * 60)

    print(reply)

    # Put generated reply into clipboard
    copy_to_clipboard(reply)

    print("\nReply copied to clipboard.")

    # Click message box
    click_message_box()

    # Paste reply
    paste_message()

    # Send
    send_message()

    print("\nMessage sent.")

    return reply