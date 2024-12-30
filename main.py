import pytesseract
import cv2


pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"
)


def preprocess_image(image_path, method="gaussian_blur"):
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if method == "median_blur":
        converted_img = cv2.medianBlur(img, 3)
    elif method == "gaussian_blur":
        converted_img = cv2.threshold(
            cv2.GaussianBlur(img, (5, 5), 0),
            0,
            255,
            cv2.THRESH_BINARY + cv2.THRESH_OTSU,
        )[1]
    elif method == "bilateral_filter":
        converted_img = cv2.threshold(
            cv2.bilateralFilter(img, 5, 75, 75),
            0,
            255,
            cv2.THRESH_BINARY + cv2.THRESH_OTSU,
        )[1]
    elif method == "adaptive_threshold":
        converted_img = cv2.adaptiveThreshold(
            cv2.GaussianBlur(img, (5, 5), 0),
            255,
            cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
            cv2.THRESH_BINARY,
            31,
            2,
        )
    elif method == "adaptive_bilateral":
        converted_img = cv2.adaptiveThreshold(
            cv2.bilateralFilter(img, 9, 75, 75),
            255,
            cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
            cv2.THRESH_BINARY,
            31,
            2,
        )
    elif method == "adaptive_median":
        converted_img = cv2.adaptiveThreshold(
            cv2.medianBlur(img, 3),
            255,
            cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
            cv2.THRESH_BINARY,
            31,
            2,
        )
    else:
        converted_img = cv2.threshold(
            cv2.GaussianBlur(img, (5, 5), 0),
            0,
            255,
            cv2.THRESH_BINARY + cv2.THRESH_OTSU,
        )[1]

    return converted_img


def ocr_from_image(image_path, method="gaussian_blur"):

    processed_image = preprocess_image(image_path, method)

    text = pytesseract.image_to_string(processed_image)
    return text


def show_image(image, window_name="Image"):
    cv2.imshow(window_name, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


image_path = "photos/1.jpg"


methods = [
    "median_blur",
    "gaussian_blur",
    "bilateral_filter",
    "adaptive_threshold",
    "adaptive_bilateral",
    "adaptive_median",
]

for method in methods:
    print(f"Testing method: {method}")
    text = ocr_from_image(image_path, method)
    print(f"Detected text using {method}: \n{text}\n")

    processed_image = preprocess_image(image_path, method)

    show_image(processed_image, f"Processed Image - {method}")
