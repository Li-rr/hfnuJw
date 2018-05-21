#!/usr/bin/python
# -*- coding:utf-8 -*-
try:
    import pytesseract
    from PIL import Image
except ImportError:
    print("模块导入失败")

def get_bin_table(threshold=140):
    """
    获取灰度转二值的映射table
    :param threshold:
    :return:
    """
    table = []
    for i in range(256):
        if i < threshold:
            table.append(0)
        else:
            table.append(1)
 
    return table

tessdata_dir_config = '--tessdata-dir "C:\\Program Files (x86)\\Tesseract-OCR\\tessdata"'
# open image
image = Image.open('code.png')

imgry = image.convert('L')
code = pytesseract.image_to_string(imgry,config=tessdata_dir_config)
print(code)