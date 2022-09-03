# Create captcha
# By Busyman.INc

#!/usr/bin/env python
# -*- coding: utf-8 -*-

from captcha.image import ImageCaptcha
image = ImageCaptcha(width = 300, height = 100)
text = input("Enter captcha:")
data = image.generate(text)
image.write(text,'captcha1.png')
from PIL import Image
Image.open('captcha1.png ')
