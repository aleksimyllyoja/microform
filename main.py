import DEV_Config
import OLED_Driver

from PIL import Image

from test_images import *

def main():
	OLED = OLED_Driver.OLED()
	OLED_ScanDir = OLED_Driver.SCAN_DIR_DFT  #SCAN_DIR_DFT = D2U_L2R

    image = Image.fromarray(test_1()).convert('L')

	OLED.OLED_Init(OLED_ScanDir)
	OLED.OLED_ShowImage(image, 0, 0)

if __name__ == '__main__':
    main()
