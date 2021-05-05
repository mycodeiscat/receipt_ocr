from typing import Text, Dict, Optional
from abc import ABC
from abc import abstractmethod

import numpy as np


class Model(ABC):
    @abstractmethod
    def train(self) -> None:
        pass

    @abstractmethod
    def predict(self, image: np.array, config: Optional[Dict]) -> Text:
        pass

    @abstractmethod
    def compute_metrics(self) -> Dict:
        pass

    @abstractmethod
    def get_params(self) -> Dict:
        pass
