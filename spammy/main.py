import pyautogui, time #pip install pyautogui
time.sleep(5)
f = open("spam_text.txt", "r")
for word in f:
    pyautogui.typewrite(word)
    pyautogui.press("enter")