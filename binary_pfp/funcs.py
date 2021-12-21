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

        # for i in range(8):
        #     for j in range(8):
        #         if j == 0:
        #             if positions[i][j] == 1:
        #                 bg.paste(clr_asset, (j * 8, i * 8))
        #             else:
        #                 bg.paste(white, (j * 8, i * 8))
        #         else:
        #             if positions[i][j] == 1:
        #                 bg.paste(clr_asset, ((j * 8) + (j * 8), (i * 8) + (i * 8)))
        #             else:
        #                 bg.paste(white, ((j * 8) + (j * 8), (i * 8) + (i * 8)))

        bg.save('profile.png')

                # elif i == 1:
                #     if positions[i][j] == 1:
                #         bg.paste(clr_asset, ((j * 8) + 8, (i * 8) + 8))
                #     else:
                #         bg.paste(white, ((j * 8) + 8, (i * 8) + 8))
                # elif i == 2:
                #     if positions[i][j] == 1:
                #         bg.paste(clr_asset, ((j * 8) + 16, (i * 8) + 16))
                #     else:
                #         bg.paste(white, ((j * 8) + 16, (i * 8) + 16))
                # elif i == 3:
                #     if positions[i][j] == 1:
                #         bg.paste(clr_asset, ((j * 8) + 24, (i * 8) + 24))
                #     else:
                #         bg.paste(white, ((j * 8) + 24, (i * 8) + 24))
                # elif i == 4:
                #     if positions[i][j] == 1:
                #         bg.paste(clr_asset, ((j * 8) + 32, (i * 8) + 32))
                #     else:
                #         bg.paste(white, ((j * 8) + 32, (i * 8) + 32))
                # elif i == 5:
                #     if positions[i][j] == 1:
                #         bg.paste(clr_asset, ((j * 8) + 40, (i * 8) + 40))
                #     else:
                #         bg.paste(white, ((j * 8) + 40, (i * 8) + 40))
                # elif i == 6:
                #     if positions[i][j] == 1:
                #         bg.paste(clr_asset, ((j * 8) + 48, (i * 8) + 48))
                #     else:
                #         bg.paste(white, ((j * 8) + 48, (i * 8) + 48))
                # elif i == 7:
                #     if positions[i][j] == 1:
                #         bg.paste(clr_asset, ((j * 8) + 56, (i * 8) + 56))
                #     else:
                #         bg.paste(white, ((j * 8) + 56, (i * 8) + 56))