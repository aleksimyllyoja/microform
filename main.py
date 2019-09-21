import DEV_Config
import OLED_Driver

from PIL import Image

from gpiozero import Button
from signal import pause


from test_images import *

def main():
	OLED = OLED_Driver.OLED()
	OLED_ScanDir = OLED_Driver.SCAN_DIR_DFT  #SCAN_DIR_DFT = D2U_L2R

	OLED.OLED_Init(OLED_ScanDir)

	def show(t=0):
		OLED.OLED_Clear()
		OLED.OLED_ShowImage(test_1(), 0, 0)
		DEV_Config.Driver_Delay_ms(t)
		OLED.OLED_Clear()

	button = Button(4)
	button.when_pressed = show

	pause()

if __name__ == '__main__':
	main()
