# Create Barcode
# by Busyman.INc

#!/usr/bin/env python
# -*- coding: utf-8 -*-

import barcode
from barcode.writer import ImageWriter

number = input("Enter the code to generate barcode: ")
bar_format = barcode.get_barcode_class('upc')
my_bar = bar_format(number, writer=ImageWriter())
my_bar.save("generated_barcode")
