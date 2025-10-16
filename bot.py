import pyautogui
import time
import pyperclip
from openai import OpenAI


client = OpenAI(
    api_key = "<Your Key Here>"
)

def is_last_message_from_sender(chat_log, sender_name="Bulbasaur"):
    # spliting chat log into individual msgs
    messages = chat_log.strip().split("/2025" )[-1]
    if sender_name in messages:
        return True
    return False


   # step 2 : Click on the chrome icon at coordinates 
   # i am using (x, y) here, but put your coordinates 
pyautogui.click(x int, y int)

time.sleep(1)  # Wait for 1 second to ensure the click is registered
while True:
    time.sleep(5)
    # step 1 : Drag the mouse from (top-left coordin8's) to 
    # (top-right coordin8's) to select the text
    pyautogui.moveTo(top-left coordinates)
    pyautogui.dragTo(top-right coordinates, duration=2.0, button='left')  # Drag for 1 second

    # Step 3: Copy the selected text to the clipboard
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(2)  # Wait for 1 second to ensure the copy command is completed
    pyautogui.click(the textbox coordinates)

    # Step 4: Retrieve the text from the clipboard and store it in a variable
    chat_history = pyperclip.paste()

    
    # Print the copied text to verify
    print(chat_history)
    print(is_last_message_from_sender(chat_history))
    if is_last_message_from_sender(chat_history):
        completion = client.chat.completions.create(
        model="gpt-5",
        messages=[
            {"role": "system", "content": "You are a person named Squirtle who speaks hindi as well as english. You are from India and you are a coder. You analyze chat history and roast people in a funny way. Output should be the next chat response (text message only)"},
            {"role": "system", "content": "Do not start like this [21:02, 12/6/2024] Bulbasaur: "},
            {"role": "user", "content": chat_history}
        ]
        )

        response = completion.choices[0].message.content
        pyperclip.copy(response)

        # Step 5: Click at coordinates (textbox coordin8's) 
        # and put here 
        pyautogui.click(textbox coordinates)
        time.sleep(1)  # Wait for 1 second to ensure the click is registered

        # Step 6: Paste the text
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(1)  # Wait for 1 second to ensure the paste command is completed

        # Step 7: Press Enter
        pyautogui.press('enter')