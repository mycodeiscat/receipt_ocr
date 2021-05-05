from abc import ABC

import numpy as np

from .base import Model
import pytesseract
from typing import Text, Optional, Dict
from pytesseract import Output


class TesseractWrapper(Model):
    def __init__(self, extractor, language='ukr'):
        self.extractor = extractor
        self.lang = language

    def train(self) -> None:
        pass

    def compute_metrics(self) -> Dict:
        pass

    def get_params(self) -> Dict:

        return {'preprocessor': self.extractor, 'lang': self.lang}

    def predict(self, image: np.array, config: Optional[Dict]) -> Text:
        """

        Args:
            image: numpy.array: original image
            config: config file containing document language

        Returns:
            extracted_text: extracted text from the document
        """
        processed_image = self.extractor(image)
        extracted_text = pytesseract.image_to_string(processed_image,
                                                     lang=config[
                                                         'lang'] if config is not None and 'lang' in config.keys() else self.lang)
        return extracted_text
