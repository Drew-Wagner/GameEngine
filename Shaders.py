from abc import ABC, abstractmethod

from OpenGL.GL import *
from OpenGL.GL import shaders


class ShaderProgram(ABC):

    def __init__(self, vertexFile, fragmentFile):
        self.vertexShaderID = ShaderProgram.loadShader(vertexFile, GL_VERTEX_SHADER)
        self.fragmentShaderID = ShaderProgram.loadShader(fragmentFile, GL_FRAGMENT_SHADER)
        self.programID = shaders.compileProgram(self.vertexShaderID, self.fragmentShaderID)
        self.bindAttributes()
        self.getAllUniformLocations()

    @abstractmethod
    def getAllUniformLocations(self):
        pass

    def getUniformLocation(self, uniformName):
        return glGetUniformLocation(self.programID, uniformName)

    @abstractmethod
    def bindAttributes(self):
        pass

    def bindAttribute(self, attribute, variableName):
        glBindAttribLocation(self.programID, attribute, variableName)

    def start(self):
        shaders.glUseProgram(self.programID)

    def stop(self):
        shaders.glUseProgram(0)

    def cleanUp(self):
        self.stop()
        glDeleteShader(self.vertexShaderID)
        glDeleteShader(self.fragmentShaderID)
        glDeleteProgram(self.programID)

    @staticmethod
    def loadShader(filename, type):
        shaderSource = ""
        with open(filename) as f:
            shaderSource = "".join(f.readlines())

        shaderID = shaders.compileShader(shaderSource, type)
        return shaderID


class StaticShader(ShaderProgram):

    VERTEX_FILE = "shaders/vertexShader"
    FRAGMENT_FILE = "shaders/fragmentShader"

    def __init__(self):
        ShaderProgram.__init__(self, self.VERTEX_FILE, self.FRAGMENT_FILE)

    def bindAttributes(self):
        self.bindAttribute(0, "position")
        self.bindAttribute(1, "textureCoords")
