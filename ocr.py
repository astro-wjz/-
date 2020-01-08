## 精确识别图片中的文字
## 通过截图将图片保存到剪贴板
## 百度API精确识别并将文字输出在命令行，同时将文字保存在剪贴板

from PIL import Image
from PIL import ImageGrab
import os
import pyperclip
from aip import AipOcr

image = ImageGrab.grabclipboard() 
image.save("screen.png")

APP_ID = '18222442'
API_KEY = '9uSHxrDZBybrBPiGtnOL0If7'
SECRET_KEY = 'z4H7iA6k6TmFtCjsWUebg9mqmtV5Po9j'

client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

print('----------------------------------------')
with open("screen.png", 'rb') as f:
    file = open("temp.txt", 'w+')
    image = f.read()
    # 调用百度API通用文字识别（高精度版），提取图片中的内容
    # text = client.basicGeneral(image)
    text = client.basicAccurate(image)
    result = text["words_result"]
    for i in result:
        #print(i["words"])
        #file.write(i["words"] + '\n')
        file.write(i["words"])
    file.close()
    file = open("temp.txt", 'r')
    contents = file.read()
    print(contents)
    pyperclip.copy(contents)
    file.close()
os.remove("screen.png")
os.remove("temp.txt")
print('----------------------------------------' + '\n')
print('Finished !')