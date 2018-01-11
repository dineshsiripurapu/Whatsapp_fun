import pyautogui

pyautogui.PAUSE = 0.1
pyautogui.FAILSAFE = True

pyautogui.moveTo(590,997,0.01)

i=0

while (i<300):
	pyautogui.typewrite('Hello chutiye\n', interval=0.01)
	#pyautogui.click(x=1253, y=999, clicks=1, interval=1, button='left')
	i=i+1;

pyautogui.typewrite('Dont worry just apython code', interval=0.01)