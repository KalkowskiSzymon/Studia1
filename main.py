import pytesseract
import cv2


pytesseract.pytesseract.tesseract_cmd = (
    r'C:\Program Files\Tesseract-OCR\tesseract.exe'
)


def preprocess_image(image_path):

    img = cv2.imread(image_path)

    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    adjusted_img = cv2.convertScaleAbs(gray_img, alpha=1.5, beta=50)

    blurred_img = cv2.GaussianBlur(adjusted_img, (5, 5), 0)

    _, thresholded_img = cv2.threshold(blurred_img,
                                       150, 255,
                                       cv2.THRESH_BINARY)

    return thresholded_img


def ocr_from_image(image_path):

    processed_image = preprocess_image(image_path)

    text = pytesseract.image_to_string(processed_image)
    return text


image_path = "photos/5.jpg"

text = ocr_from_image(image_path)


print(text)
