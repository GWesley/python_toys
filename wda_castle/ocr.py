import pytesseract
from PIL import Image
import re


digits = re.sub('\D', "", "101023aab")
print(type(digits))


img = Image.open('screen.png')
# box1 = (660,910,900,975)
# crop1 = img.crop(box1)
gray = img.convert('L')
ww = gray.point(lambda x:255 if x >= 230 else 0, '1')
# text = pytesseract.image_to_string(ww).replace(' ','')
# print(int(text))

#
#
ww.save('ocr_w2.png')