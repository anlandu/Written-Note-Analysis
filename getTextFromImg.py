try:
    import Image
except ModuleNotFoundError:
    from PIL import Image
import pytesseract
import sys
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract'
try:
    print(pytesseract.image_to_string(Image.open(sys.argv[1])))
except:
    print("File not found")
