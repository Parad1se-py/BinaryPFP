import random
import PIL

class Maker:
    def __init__(self, color):
        self.color = color.lower()

    @staticmethod
    def bit_32_maker():
        color = Maker.color