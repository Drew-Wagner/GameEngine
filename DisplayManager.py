import pygame
import OpenGL

from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

WIDTH = 1280
HEIGHT = 720
FPS_CAP = 60
TITLE = "Our first display"
CLOCK = None

def createDisplay():
    """Initilizes PyGame and OpenGL"""
    global CLOCK
    pygame.init()
    CLOCK = pygame.time.Clock()
    display = (WIDTH, HEIGHT)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    pygame.display.set_caption(TITLE)

    glViewport(0, 0, WIDTH, HEIGHT)
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)

def updateDisplay():
    """Flips the display and limits FPS"""
    pygame.display.flip()
    CLOCK.tick(FPS_CAP)

def closeDisplay():
    """Handles any necessary exit/clean up tasks"""
    pygame.quit()
