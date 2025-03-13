# ai_model/ocr/tesseract.py
import pytesseract
from PIL import Image
import cv2

def ocr_pipeline(image_path):
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    text = pytesseract.image_to_string(gray)
    return text