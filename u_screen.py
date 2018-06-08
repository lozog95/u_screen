import pyscreenshot as ps
from pynput.mouse import Listener
from datetime import datetime

def on_click(x,y, button, pressed):
	now=datetime.now()
	h=str(now.hour)
	m=str(now.minute)
	s=str(now.second)
	ss=ps.grab()
	ss.save('screen'+h+"_"+m+"_"+s+'.png')

with Listener (on_click=on_click) as listener:
	listener.join()
