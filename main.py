from utils.hough_line_corner_detector import HoughLineCornerDetector
from utils.processors import Resizer, OtsuThresholder, FastDenoiser
from utils.page_extractor import PageExtractor
import cv2
import pytesseract

if __name__ == "__main__":
    page_extractor = PageExtractor(
        preprocessors=[
            Resizer(height=1280, output_process=True),
            FastDenoiser(strength=10, output_process=True),
            OtsuThresholder(output_process=True)
        ],
        corner_detector=HoughLineCornerDetector(
            rho_acc=1,
            theta_acc=180,
            thresh=100,
            output_process=True
        )
    )
    path = 'C:\\Users\\depem\\Downloads\\receipt2.jpg'
    extracted = page_extractor(path)
    extracted_string = pytesseract.image_to_string(extracted, lang="ukr")
    print(extracted_string)
    cv2.imshow("Extracted page", extracted)
    cv2.waitKey(0)
