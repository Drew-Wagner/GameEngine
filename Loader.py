import pygame

import OpenGL

from OpenGL.GL import *
from OpenGL.GLU import *

from array import array
from RawModel import RawModel

class Loader:

    def __init__(self):
        self.vaos = []
        self.vbos = []
        self.textures = []

    def loadToVao(self, positions, textureCoords, indices):
        """Creates a VAO and stores the position data of vertices into attribute 0 of VAO

        :param positions: The 3D positions of each vertex in the geometry
        :type positions: List of Vector3

        :return: The loaded model
        :rtype: RawModel
        """
        vaoID = self.createVAO()
        self.bindIndicesBuffer(indices)
        self.storeDataInAttributeList(0, 3, positions)
        self.storeDataInAttributeList(1, 2, textureCoords)
        return RawModel(vaoID, len(indices))

    def loadTexture(self, fileName):
        image = pygame.image.load(fileName)
        textureData = pygame.image.tostring(image, "RGBA", 1)
        width = image.get_width()
        height = image.get_height()

        glEnable(GL_TEXTURE_2D)

        textureID = glGenTextures(1)
        glBindTexture(GL_TEXTURE_2D, textureID)
        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, width, height, 0, GL_RGBA, GL_UNSIGNED_BYTE, textureData)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
        self.textures.append(textureID)
        return textureID

    def cleanUp(self):
        """ Deletes all the VAOs and VBOs when the program is closed. VAOs and VBOs are
        located in video memory.
        """
        glDeleteVertexArrays(len(self.vaos), self.vaos)

        glDeleteBuffers(len(self.vbos), self.vbos)

        glDeleteTextures(self.textures)

    def createVAO(self):
        """Creates a new VAO and returns the ID.

        :return: The ID of the newly create VAO
        :rtype: int
        """
        vaoID = glGenVertexArrays(1)
        self.vaos.append(vaoID)
        glBindVertexArray(vaoID)
        return vaoID

    def storeDataInAttributeList(self, attributeNumber, coordinateSize, data):
        """Stores data in specified attribute list of a newly generated VBO

        :param attributeNumber: The number of the attribute of the VAO where the data will be stored
        :type attributeNumber: int
        :param data: The data to be stored in the VAO
        :type data: list of floats
        """
        vboID = glGenBuffers(1)
        self.vbos.append(vboID)
        glBindBuffer(GL_ARRAY_BUFFER, vboID)

        glBufferData(GL_ARRAY_BUFFER, data.nbytes, data, GL_STATIC_DRAW)
        glVertexAttribPointer(attributeNumber, coordinateSize, GL_FLOAT, GL_FALSE, 0, None)

        # Unbind buffer once we are finished
        glBindBuffer(GL_ARRAY_BUFFER, 0)

    def unbindVAO(self):
        glBindVertexArray(0)

    def bindIndicesBuffer(self, indices):
        vboID = glGenBuffers(1)
        self.vbos.append(vboID)
        glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, vboID)
        glBufferData(GL_ELEMENT_ARRAY_BUFFER, indices.nbytes, indices, GL_STATIC_DRAW)

