import cv2 
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def extract():
    img = cv2.imread('img.png')

    # Adding custom options
    custom_config = r'--oem 3 --psm 6'
    boxes = pytesseract.image_to_boxes(img, config=custom_config)
    print(boxes)
    return  pytesseract.image_to_string(img, config=custom_config)


if __name__ == "__main__":
    print(extract())