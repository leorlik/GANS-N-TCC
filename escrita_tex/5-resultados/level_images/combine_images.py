from PIL import Image
import os
import sys


def combine_images(columns, space, images, image_name, direc):
    rows = len(images) // columns
    if len(images) % columns:
        rows += 1
    width_max = max([Image.open(os.path.join(direc, image)).width for image in images])
    height_max = max([Image.open(os.path.join(direc, image)).height for image in images])
    background_width = width_max*columns + (space*columns)-space
    background_height = height_max*rows + (space*rows)-space
    background = Image.new('RGBA', (background_width, background_height), (255, 255, 255, 255))
    x = 0
    y = 0
    for i, image in enumerate(images):
        img = Image.open(os.path.join(direc, image))
        x_offset = int((width_max-img.width)/2)
        y_offset = int((height_max-img.height)/2)
        background.paste(img, (x+x_offset, y+y_offset))
        x += width_max + space
        if (i+1) % columns == 0:
            y += height_max + space
            x = 0
    background.save(image_name)


if __name__ == '__main__':
    combine_images(columns=2, space=20, images=os.listdir(sys.argv[1]), image_name = sys.argv[2], direc = sys.argv[1])
