class RawModel:

    def __init__(self, vaoID, vertexCount):
        """RawModel Constructor

        :param vaoID: The ID of the VAO where the model data is stored
        :type vaoID: int
        :param vertexCount: The number of vertices in the model
        :type vertexCount: int
        """

        self.vaoID = vaoID
        self.vertexCount = vertexCount

    def getVaoID(self):
        return self.vaoID

    def getVertexCount(self):
        return self.vertexCount