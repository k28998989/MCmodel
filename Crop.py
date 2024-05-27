import cv2
import random
from PIL import Image
def ranCrop(anchor_img, positive_img):
    r = random.random()
    if r > 0.5:
        img = Crop(anchor_img)
        return img, positive_img
    else:
        img = Crop(positive_img)
        return anchor_img, img

def Crop(img):
    r = random.random()
    w, h=img.size
    left = 0
    top = 0
    if r < 0.2: #上半
        croppingImg = img.crop((left, top, w, h/2))
    elif r < 0.4: #左半
        croppingImg = img.crop((left, top, w/2, h))
    elif r < 0.6: #右半
        croppingImg = img.crop((w/2, top, w, h))
    elif r < 0.8: #左上
        croppingImg = img.crop((left, top, w/2, h/2))
    else: #右上
        croppingImg = img.crop((w/2, top, w, h/2))
    return croppingImg

# 讀取圖檔
img1 = Image.open("0/18.jpg")
img2 = Image.open("0/2.jpg")
# cv2.imshow("cropped", img1) 
# cv2.imshow("cropped", img2)
img1, img2 = ranCrop(img1, img2)

img1.save('test1.jpg')
img2.save('test2.jpg')