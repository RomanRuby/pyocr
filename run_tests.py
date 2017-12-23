#!/usr/bin/env python3
import codecs
import sys

sys.path = ["src"] + sys.path
import PIL.Image
import pyocr
import PIL.Image
from pyocr import builders, libtesseract
from pyocr import pyocr


if __name__ == '__main__':
    for tool in pyocr.TOOLS:
        print("- OCR: %s" % tool.get_name())
        available = tool.is_available()
        print("  is_available(): %s" % (str(available)))
        if available:
            print("  get_version(): %s" % (str(tool.get_version())))
            print("  get_available_languages(): ")
            print("    " + ", ".join(tool.get_available_languages()))
        print("")
    print("")
    print("OCR tool found:")
    for tool in pyocr.get_available_tools():
        txt = tool.image_to_string(
            PIL.Image.open('2.jpg'),
            lang="eng",
            builder=builders.DigitBuilder(),
        )
        print('text', txt)
        print("- %s" % tool.get_name())
    # if libtesseract.is_available():
    #     print("---")
    #     print("Tesseract C-API:")
    #     unittest.TextTestRunner().run(tests_libtesseract.get_all_tests())
    # if tesseract.is_available():
    #     print("---")
    #     print("Tesseract SH:")
    #     unittest.TextTestRunner().run(tests_tesseract.get_all_tests())
    # if cuneiform.is_available():
    #     print("---")
    #     print("Cuneiform SH:")
    #     unittest.TextTestRunner().run(tests_cuneiform.get_all_tests())
