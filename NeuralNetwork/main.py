import pygame as pg
from PIL import Image, ImageEnhance
import pytesseract

pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'

pg.init()
sc = pg.display.set_mode((500, 500))
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
sc.fill(WHITE)
pg.display.update()

play = True
while play:
    for i in pg.event.get():
        if i.type == pg.QUIT:
            pg.quit()
            play = False
        if i.type == pg.MOUSEBUTTONDOWN:
            if i.button == 3:
                pg.image.save(sc, 'result.jpg')
                image = Image.open('result.jpg')

                print(pytesseract.image_to_string(image, lang='eng',config='--psm 10 --oem 3 -c tessedit_char_whitelist=0123456789'))

            if i.button == 2:
                sc.fill(WHITE)
                pg.display.update()
    if play:
        cur = pg.mouse.get_pos()
        click = pg.mouse.get_pressed()
        if click[0] == True:
            pg.draw.circle(sc, BLACK, (cur[0], cur[1]), 10)
        pg.display.update()