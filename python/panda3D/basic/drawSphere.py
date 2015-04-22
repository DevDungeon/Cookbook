from direct.showbase.ShowBase import ShowBase
import sys

class MyApp(ShowBase):
 
    def __init__(self):
        ShowBase.__init__(self)
        base.setBackgroundColor(.5, 0.0, 0.0)
        # Load the environment model.
        self.environ = self.loader.loadModel("models/misc/sphere")
        # Reparent the model to render.
        self.environ.reparentTo(self.render)
        # Apply scale and position transforms on the model.
        self.environ.setPos(-8, 42, 0)
        self.environ.setColor(0,1,0) # Make green


        base.accept("escape", sys.exit)
 
app = MyApp()
app.run()
