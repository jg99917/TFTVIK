import pytesseract as pyte
from PIL import ImageGrab
import pyautogui as pyat
import time

pyte.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract'

def store(camp):
    time.sleep(0.12)
    store = [ImageGrab.grab((480,1038,580,1068)),ImageGrab.grab((682,1038,782,1068)),ImageGrab.grab((884,1038,984,1068)),ImageGrab.grab((1086,1038,1186,1068)),ImageGrab.grab((1288,1038,1388,1068))]
    for i in range(5):
        store[i] = store[i].convert('L')
        check = pyte.pytesseract.image_to_string(store[i], lang='KOR',config='--psm 4 -c preserve_interword_spaces=1').split('\n')[0].strip()
        if check in camp:
            pyat.mouseDown(500+202*i,1000)
            pyat.mouseUp()