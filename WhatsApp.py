from sre_constants import SUCCESS
from telnetlib import SUPPRESS_LOCAL_ECHO
import pyautogui
import webbrowser as wb
import time 

wb.open("web.whatsapp.com")
time.sleep(25)
for i in range(5):
    pyautogui.press("s")
    pyautogui.press("p")
    pyautogui.press("a")
    pyautogui.press("m")
    pyautogui.press("enter")



