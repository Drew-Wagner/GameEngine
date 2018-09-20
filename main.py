### Python implementation of ThinMatrix's OpenGL game engine tutorial
### Credit: github.com/TheThinMatrix/

import numpy as np

import pygame
import OpenGL

from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GL import shaders
from OpenGL.GLU import *

import DisplayManager
from Loader import Loader
from ModelTexture import ModelTexture
from Renderer import Renderer
from Shaders import StaticShader

# Initialize pygame and OpenGL
from TexturedModel import TexturedModel

DisplayManager.createDisplay()

loader = Loader()
renderer = Renderer()

shader = StaticShader()

vertices = np.array([
    -0.5, 0.5, 0,
    - 0.5, -0.5, 0,
    0.5, -0.5, 0,
    0.5, 0.5, 0
], dtype=np.float32)

indices = np.array([0, 1, 3, 3, 1, 2], dtype=np.uint32)

textureCoords = np.array([0,0,
                          0,1,
                          1,1,
                          1,0], dtype = np.float32)

rawModel = loader.loadToVao(vertices, textureCoords, indices)
texture = ModelTexture(loader.loadTexture("res/dirt.png"))
texturedModel = TexturedModel(rawModel, texture)

quitRequested = False
while not quitRequested:
    # Keyboard / Mouse input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quitRequested = True

    # Game logic
    pass

    # Render logic
    renderer.prepare()
    shader.start()
    renderer.render(texturedModel)
    shader.stop()
    DisplayManager.updateDisplay()

# Exit the program
shader.cleanUp()
loader.cleanUp()
DisplayManager.closeDisplay()
quit()
