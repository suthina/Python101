import pyautogui as pg
import webbrowser
import time
import pyperclip
from datetime import datetime

url = 'https://www.google.com'
webbrowser.open(url)
time.sleep(2)

#pg.write('weather in chiangmai',interval=0.25)
keyword = 'อุณหภูมิเชียงใหม่'
pyperclip.copy(keyword)
time.sleep(1)

pg.hotkey('ctrl','v')
time.sleep(1)


pg.press('enter')
time.sleep(2)

stamp = datetime.now().strftime('%Y-%m-%d %H%M%S')
file = 'capture-{}.png'.format(stamp)
#path = 'C:\\Users\\ACER\\Desktop\\suthina\\'
#pg.screenshot(path+file)
pg.screenshot(file)

