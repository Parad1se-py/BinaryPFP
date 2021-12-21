import os
import random
from io import BytesIO

import PIL
from PIL import Image

import binary_pfp.pos as pos


class ImageMaker:
    def __init__(self, color):
        self.color = color.lower()

    def bit_64_maker(self):
        color = self.color
        bg = Image.open('./assets/imgs/64-64.png')
        clr_asset = Image.open('./assets/imgs/' + color + '.png')
        white = Image.open('./assets/imgs/white.png')

        positions = pos.create_pos_lists()

        for i in range(len(positions)):
            for j in range(len(positions[i])):
                if positions[i][j] == 1:
                    bg.paste(clr_asset, (j * 8, i * 8))
                else:
                    bg.paste(white, (j * 8, i * 8))

        bg.save('profile.png')