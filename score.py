import pygame
from colors import *
from fonts import *
from display import *


def Your_score(score):
    value = score_font.render("Score: " + str(score), True, white)
    dis.blit(value, [0, 0])