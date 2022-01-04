from colors import *
from display import *
from fonts import *

def message(msg, color):
    msg = font_style.render(msg, True, color)
    dis.blit(msg, [dis_width / 8, dis_height / 3])