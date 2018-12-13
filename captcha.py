# -*- coding: utf-8 -*-

import os
import sys
import random
from PIL import Image, ImageDraw, ImageFont

LETTERSTR = '0123456789ABCDEFGHJKLMNPQRSTUVWXYZ'

#create empty image (has background)
def background_color():
    list = []
    for _ in range(0,3):
        list.append(random.randint(80,255))
    return tuple(list)

#draw letter
def random_captcha_text(letter_str, size):
    text = []
    for i in range(size):
        c = random.choice(letter_str)
        text.append(c)
    return text

def draw_letter (draw, coord, letter):
    fontsize = 32
    font = ImageFont.truetype("arial.ttf", fontsize)
    letter_color = (28, 28, 28)  # like black
    draw.text(coord, ''.join(letter), fill=letter_color, font=font, anchor=None)

#create image
def main():
    current_path = os.getcwd()
    print(current_path)
    new_path = current_path + '\\' + sys.argv[1]
    print(new_path)
    os.mkdir(new_path)
    os.chdir(new_path)
    
    for _ in range(0, int(sys.argv[2])):
        #create background
        bg = background_color()
        ct = 'RGBA'
        size = (160, 90)
        im = Image.new(ct, size, bg) 
    
        #draw line
        line_num = random.randint(16,22)
        draw = ImageDraw.Draw(im)
        for i in range(1, line_num):
            line_width = random.randint(14,17)
            line_x1 = ((random.randint(0,40),random.randint(0,90)))
            line_x2 = ((random.randint(120,160),random.randint(0,90)))
            line_x = [line_x1, line_x2]
            line_color = (random.randint(110,250), random.randint(110,250), random.randint(110,250))
            draw.line(line_x, fill = line_color, width = line_width)
            le = random_captcha_text(LETTERSTR, 4)
            gap = 0
            
        #draw letter
        text_coord_test = []
        for j in range(0,4):
            xy = ((random.randint(10+gap,20+gap),random.randint(23,36)))
            draw_letter(draw, xy, le[j])
            text_coord_test.append(xy)
            gap = gap + random.randint(35,40)
    
        #save image
        im.save(''.join(le)+'.bmp')
    
if __name__ == "__main__":
    main()







