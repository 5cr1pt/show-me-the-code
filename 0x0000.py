# encoding: utf-8

from PIL import Image, ImageDraw, ImageFont

input_file = "0x0000.png"
output_file = "0x0001.png"
font_dir = "/Users/super/Library/Fonts/PingHei-text.ttf"


# im = Image.open(input_file)

def addNum(img):
    draw = ImageDraw.Draw(img)
    color = "#ff0000"
    weight, height = img.size
    fnt = ImageFont.truetype(font_dir, 20)
    draw.text((weight - 40, 10), "1024", font=fnt, fill=color)
    img.save(output_file, 'jpeg')
    Image.open(output_file).show()


if __name__ == '__main__':
    img = Image.open(input_file)
    addNum(img)
