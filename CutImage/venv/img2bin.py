#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
图片处理成32x32的二进制数据
'''
from PIL import Image

# 打开要处理的图像
img_src = Image.open('5.png')
size = img_src.size
# 转换图片的模式为RGBA
img_src = img_src.convert('RGB')
L, H = img_src.size

with open('1.bin','wb') as f:
    for i in range(H):
        for j in range(L):
            tmp = img_src.getpixel((j, i))
            if(tmp != (255, 255, 255)):
                f.write(b'1')
            else:
                f.write(b'0')