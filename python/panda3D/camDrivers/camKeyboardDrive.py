from math import pi, sin, cos
import sys
from direct.showbase.ShowBase import ShowBase
from direct.task import Task
 
class MyApp(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        
       
        # Load the environment model.
        self.environ = self.loader.loadModel("models/environment")
        self.environ.reparentTo(self.render)
        self.environ.setScale(0.25, 0.25, 0.25)
        self.environ.setPos(-8, 42, 0)

        # Disable default mouse/camera task
        self.disableMouse()
        self.accept("w", self.startMoveForward)
        self.accept("w-up", self.stopMoveForward)
        self.accept("a", self.startMoveLeft)
        self.accept("a-up", self.stopMoveLeft)
        self.accept("d", self.startMoveRight)
        self.accept("d-up", self.stopMoveRight)
        self.accept("s", self.startMoveBack)
        self.accept("s-up", self.stopMoveBack)
        
        self.accept("escape", sys.exit)
        self.taskMgr.add(self.playerControlTask, "playerControlTask")

        # self.User is a dummy node to attach camera to
        self.Player = render.attachNewNode('Player')
        self.camera.reparentTo(self.Player)
        
        #default movement setting
        self.movingForward = False
        self.movingLeft = False
        self.movingRight = False
        self.movingBack = False
                        
    def startMoveForward(self):
        self.movingForward = True

    def stopMoveForward(self):
        self.movingForward = False

    def startMoveBack(self):
        self.movingBack = True

    def stopMoveBack(self):
        self.movingBack = False

    def startMoveLeft(self):
        self.movingLeft = True
        
    def stopMoveLeft(self):
        self.movingLeft = False

    def startMoveRight(self):
        self.movingRight = True
        
    def stopMoveRight(self):
        self.movingRight = False



    def playerControlTask(self, task):
        """
        Handle movement
        constantly move somewhere (or nowhere)
        keydown will trigger movement, keyup will trigger stop
        
        """        
        if self.movingForward == True:
            self.Player.setPos(self.Player, 0, 0.1, 0)
        if self.movingBack == True:
            self.Player.setPos(self.Player, 0, -0.1, 0)
        if self.movingLeft == True:
            self.Player.setPos(self.Player, -0.1, 0, 0)
        if self.movingRight == True:
            self.Player.setPos(self.Player, 0.1, 0, 0)

        return task.cont
   
app = MyApp()
app.run()
