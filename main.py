
import pywhatkit as send
import datetime
import pyautogui as pg

x = datetime.datetime.now()

min = x.strftime("%M")
hour = x.strftime("%H")
h = int(hour)
m = int(min)


phone = "+330789548628"
text = "bonsoir"

send.sendwhatmsg(phone,text,h,m+1)
pg.press("enter")
