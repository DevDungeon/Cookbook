from math import pi, sin, cos
import sys
from direct.showbase.ShowBase import ShowBase
from direct.task import Task
from panda3d.core import WindowProperties, ModifierButtons
 
class MyApp(ShowBase):

    def __init__(self):

        # Default Panda3D world init
        ShowBase.__init__(self)
       
        # Load the environment model.
        self.environ = self.loader.loadModel("models/environment")
        self.environ.reparentTo(self.render)
        self.environ.setScale(0.25, 0.25, 0.25)
        self.environ.setPos(-8, 42, 0)

        # Player node to attach camera to
        self.Player = render.attachNewNode('Player')
        self.fpsController = fpsController(self.Player)

class fpsController():

    def __init__(self, playerNP):

        # Store player and reparent camera
        self.Player = playerNP
        # Attach camera to parent
        base.camera.reparentTo(self.Player)

        # Default variables
        self.movingForward = False
        self.movingLeft = False
        self.movingRight = False
        self.movingBack = False
        self.movingUp = False
        self.baseSpeed = 0.2 # basis for all relative speed calcs
        self.moveSpeed = self.baseSpeed
        self.mouseSensitivity = 0.2

        # Hide the cursor
        self.props = WindowProperties()
        self.props.setCursorHidden(True)
        base.win.requestProperties(self.props)
        self.handleWindowResize() # Set center x/y to pull cursor to

        # Disable modifier keys like shift so I can use manually
        # and they don't throw a shift-x event instead
        base.buttonThrowers[0].node().setModifierButtons(ModifierButtons())
        # Disable default mouse/camera task
        base.disableMouse()
        base.accept("w", self.startMoveForward)
        base.accept("w-up", self.stopMoveForward)
        base.accept("a", self.startMoveLeft)
        base.accept("a-up", self.stopMoveLeft)
        base.accept("d", self.startMoveRight)
        base.accept("d-up", self.stopMoveRight)
        base.accept("s", self.startMoveBack)
        base.accept("s-up", self.stopMoveBack)
        base.accept("space", self.startMoveUp)
        base.accept("space-up", self.stopMoveUp)
        base.accept("shift", self.startMoveFast)
        base.accept("shift-up", self.stopMoveFast)
        base.accept("escape", sys.exit)
        base.accept("window-resize", self.handleWindowResize)

        # Player control task
        base.taskMgr.add(self.playerControlTask, "playerControlTask")
        
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

    def startMoveUp(self):
        self.movingUp = True

    def stopMoveUp(self):
        self.movingUp = False

    def startMoveFast(self):
        self.moveSpeed = self.baseSpeed * 4

    def stopMoveFast(self):
        self.moveSpeed = self.baseSpeed

    def handleWindowResize(self):
        # Change center x,y if window is resized
        props = base.win.getProperties()
        self.centerX  = props.getXSize() / 2
        self.centerY = props.getYSize() / 2

    def playerControlTask(self, task):
        """
        Handle movement
        constantly move somewhere (or nowhere)
        keydown will trigger movement, keyup will trigger stop
        """
        # Keyboard movement
        if self.movingForward == True:
            self.Player.setPos(self.Player, 0, self.moveSpeed, 0)
        if self.movingBack == True:
            self.Player.setPos(self.Player, 0, -self.moveSpeed, 0)
        if self.movingLeft == True:
            self.Player.setPos(self.Player, -self.moveSpeed, 0, 0)
        if self.movingRight == True:
            self.Player.setPos(self.Player, self.moveSpeed, 0, 0)
        if self.movingUp == True:
            self.Player.setPos(self.Player, 0, 0, self.moveSpeed)

        # Mouse camera direction control
        # Change HPR based on mouse movement
        m = base.win.getPointer(0)
        x = m.getX()
        y = m.getY()
        if base.win.movePointer(0, self.centerX, self.centerY): 
            self.Player.setH(self.Player.getH() -
                             (x - self.centerX) * self.mouseSensitivity)
            self.Player.setP(self.Player.getP() -
                             (y - self.centerY) * self.mouseSensitivity)

        return task.cont
   
app = MyApp()
app.run()
