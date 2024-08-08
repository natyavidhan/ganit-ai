import pytesseract
import pygame
from PIL import Image

import io

def conv_pillow(surf: pygame.Surface):
    bytes_data = pygame.image.tostring(surf, "RGBA")
    return Image.frombytes("RGBA", surf.get_size(), bytes_data)

def ocr(surf, coords):
    img = conv_pillow(surf)
    img = img.crop((coords[0], coords[1], coords[0]+coords[2], coords[1]+coords[3]))
    # img.show()
    img.save("save.png")
    text = pytesseract.image_to_string(img)
    return text