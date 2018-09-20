class TexturedModel:

    def __init__(self, model, texture):
        self.rawModel = model
        self.texture = texture

    def getRawModel(self):
        return self.rawModel

    def getTexture(self):
        return self.texture