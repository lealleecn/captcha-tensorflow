from PIL import Image,ImageDraw,ImageFont,ImageOps
import cv2
import numpy as np
import os

def generateImage(text, imgWidth, imgHeight, fileName):
    img = Image.new('RGB', (imgWidth, imgHeight), 'white')
    # 创建画刷，用来写文字到图片img上
    draw = ImageDraw.Draw(img)
    #创建字体，fontFile为字体文件，若非系统字体需加详细路径
    font = ImageFont.truetype(os.path.abspath('datasets/fonts/simsun.ttf'), 16)
    #获得文件的大小
    textWidth,textHeight=font.getsize(text)
    # 初始左上角的坐标
    leftTop =  ((imgWidth - textWidth) // 2, (imgHeight - textHeight) // 2)
    #绘图　　　　　　　　　　　　　　　　　
    draw.text(leftTop, text, font=font, fill=(0, 0, 0))
    # img.save(fileName, 'png')
    np.array(img)
    # threshold：将图像二值化为黑白图片
    _ret, binaryImage = cv2.threshold(
        np.array(img), 250, 255, cv2.THRESH_BINARY)
    cv2.imwrite(fileName, binaryImage)



# generateImage('1a')
# generateImage('赣s')
