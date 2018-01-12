#first open whatsapp on your desktop (whatsapp web) open that person account to whome you want to send the messages
#specify the coordinates (given below how to know coordinates) where mouse should click first to write
#Enjoy 
#caution- Don't specify the range in Lakhs it may crash your friends whatsapp 



import pyautogui                      #Module to control mouse and keyboard

pyautogui.PAUSE = 1				      #time(in seconds) that specify the duration between any two pyautogui function 
pyautogui.FAILSAFE = True			  #if something unexpected happens than we can raise fail safe exception by 
									  #simply moving mouse upper left-top corner 

pyautogui.moveTo(590,997,0.01)        #this statements say to move mouse on that coordinate
									  #if you want to know at what point what is the coordinate then run following
									  #command on your terminal
									  #1.first run python3 interpreter
									  #2.import pyautogui
									  #3.pyautogui.displayMousePosition()
									  #it will not only display mouse position but also 
									  #show RGB value where the mouse is present 

i=0
while (i<300):						  #range how many times you want to send the msg
	pyautogui.typewrite('Hello world\n', interval=1)			#this statement writes and send your message 
	i=i+1;

pyautogui.typewrite('Dont worry just apython code', interval=1)	