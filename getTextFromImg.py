try:
    import Image
except ModuleNotFoundError:
    from PIL import Image
import pytesseract
import sys
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract'
from wand.image import Image
class GetText:
    def getText(filename):
        if ".jpeg" in filename or ".jpg" in filename:
            try:
                print(pytesseract.image_to_string(Image.open(filename)))
            except:
                print("File not found")
        elif ".pdf" in filename:
            with Image(filename="output.jpeg", resolution=300) as image_jpeg:
                image_jpeg.compression_quality = 99
                image_jpeg = image_pdf.convert('jpeg')
                # for each page, convert that page to an image and append to blob
                for img in image_jpeg.sequence:
                    img_page = Image(image=img)
                    req_image.append(img_page.make_blob('jpeg'))
                    print(pytesseract.image_to_string(Image.open(image_jpeg)))
