import io
from typing import Text, AnyStr, Dict, Optional
import cv2
import numpy as np
from PIL import Image

from utils.hough_line_corner_detector import HoughLineCornerDetector
from utils.processors import Resizer, OtsuThresholder, FastDenoiser, Erosion, Opener
from utils.page_extractor import PageExtractor
from models.tesseract import TesseractWrapper

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

model = TesseractWrapper(page_extractor)


def image_to_text(file, config: Dict) -> AnyStr:
    """
    Sends image to OCR processing pipeline
    Args:
        config: model configuration
        file: Encoded image

    Returns:
        Extracted text from OCR image processing
    """
    image = cv2.imdecode(np.frombuffer(file.read(), np.uint8), cv2.IMREAD_UNCHANGED)
    return model.predict(image, config)
