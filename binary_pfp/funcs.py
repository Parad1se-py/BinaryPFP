import PIL
from PIL import Image

import binary_pfp.pos as pos


class ImageMaker:
    """
    This is a class for making Binary PFPs.

    Attributes:
        color (str): The color of the PFP.
    """

    def __init__(self, color):
        """
        Initializes the ImageMaker class.

        Parameters:
            color (str): The color of the PFP.
        """
        self.color = color.lower()

    def bit_64_maker(self):
        """
        Makes a 64x64 image using the function in binary_pfp\pos.py.

        It uses the function in binary_pfp\pos.py to make a 64x64 image
        of the 64x64 array of 0 and 1 integers. It then converts the
        image to a PIL image and saves it as a PNG file.

        Parameters:
        None

        Returns:
        None, just saves an image.
        """
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