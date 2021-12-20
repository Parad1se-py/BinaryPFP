import random
from io import BytesIO

import PIL
from PIL import Image

import pos


class ImageMaker:
    def __init__(self, color):
        self.color = color.lower()

    async def bit_32_maker(self):
        color = self.color
        bg = Image.open('./alki/assets/img/32-32.png')
        color = Image.open('./alki/assets/img/' + color + '.png')

        positions = pos.create_pos_lists()

        data = BytesIO(await color.read())
        clr_asset = Image.open(data)

        for i in range(4):
            for j in range(4):
                if positions[i][j] == 1:
                    bg.paste(clr_asset, (j * 32, i * 32))

        for i in positions:
            i.reverse()

        bg.save('profile.png')

positions = pos.create_pos_lists()