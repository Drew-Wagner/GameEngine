import OpenGL
from OpenGL.GL import *
from OpenGL.GLU import *

class Renderer:

    def prepare(self):
        """This method is called each frame before any rendering. It clears the screen of
        anything that was rendered on a previous frame."""
        glClear(GL_COLOR_BUFFER_BIT)
        glClearColor(0.0, 0.0, 0.0, 1.0)


    def render(self, texturedModel):
        """Renders a model to the screen.

        :param model: the model to be rendered
        :type model: RawModel
        """
        model = texturedModel.getRawModel()
        glBindVertexArray(model.getVaoID())
        glEnableVertexAttribArray(0)
        glEnableVertexAttribArray(1)
        glActiveTexture(GL_TEXTURE0)
        glBindTexture(GL_TEXTURE_2D, texturedModel.getTexture().getID())
        glDrawElements(GL_TRIANGLES, model.getVertexCount(), GL_UNSIGNED_INT, None)
        glDisableVertexAttribArray(0)
        glDisableVertexAttribArray(1)
        glBindVertexArray(0)

