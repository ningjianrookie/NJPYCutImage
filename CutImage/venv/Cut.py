import cv2
import random

from PIL import Image


def gen_image(image_name):
    # 读取图片
    img = cv2.imread(image_name)
    imageWidth = 1280
    imageHeight = 720
    count = 1
    while 1:
        # 随机产生x,y  此为像素内范围产生
        y = random.randint(1, imageHeight)
        x = random.randint(1, imageWidth)

        # h、w为想要截取的图片大小
        h = random.randint(100, 300)
        w = random.randint(100, 300)
        # 随机截图
        randomX = imageWidth if (x+w) > imageWidth else (x + w)
        randomY = imageHeight if (y+h) > imageHeight else (y+h)

        crop_img = img[y:randomY, x:randomX]

        image_file_name = random_string() + '_00' + str(count)
        cv2.imwrite('pic/' + image_file_name + '.png', crop_img)
        # gen_bin(image_file_name)
        count += 1

        if count == 200:
            break


def random_string():
    # 大写字母+小写字母+数字
    value = ''
    list = [chr(i) for i in range(65, 91)] + [chr(i) for i in range(97, 123)] + [str(i) for i in range(10)]
    num = random.sample(list, 10)
    value = value.join(num)
    return value


def gen_bin(image_name):
    # 打开要处理的图像
    img_src = Image.open('pic/' + image_name + '.png')
    # 转换图片的模式为RGBA
    img_src = img_src.convert('RGB')
    L, H = img_src.size

    with open('bin/' + image_name + '.bin', 'wb') as f:
        for i in range(H):
            for j in range(L):
                tmp = img_src.getpixel((j, i))
                if (tmp != (255, 255, 255)):
                    f.write(b'1')
                else:
                    f.write(b'0')


# for i in ["1.png", "2.png", "3.png", "4.png", "5.png"]:
for i in ["5.png"]:
    gen_image(i)

# for i in ["0506.png"]:
#     gen_image(i)
