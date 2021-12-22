from binary_pfp.funcs import ImageMaker

color = input("What do you want as the color?\n\t>>> ")

avatar = ImageMaker(color)
avatar.bit_64_maker()

print("PFP made!")