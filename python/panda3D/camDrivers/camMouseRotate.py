from panda3d.core import WindowProperties
from direct.showbase.ShowBase import ShowBase
from math import pi, sin, cos, tan

class MyApp(ShowBase):

    def __init__(self):
        ShowBase.__init__(self)

        self.player= base.loader.loadModel("models/teapot")
        self.camController = CamController(self.player)

class CamController():

    def __init__(self, parent):
        # Reparent camera to nodepath passed
        self.parent = parent
        base.camera.reparentTo(self.parent)
        # Turn off default mouse driver
        base.disableMouse()
        # Mouse and window positions
        bprops = base.win.getProperties()
        self.centerX  = bprops.getXSize() / 2
        self.centerY = bprops.getYSize() / 2
        self.storedMouseX = self.centerX # Default to center
        self.storedMouseY = self.centerY
        # Window properties used to turn mouse cursor on/off
        self.props = WindowProperties()
        # Defaults
        self.camControl = False
        self.camDistance = 30
        self.zoomSpeed = 3
        self.zoomMax = 100
        self.zoomMin = 0
        self.xDegrees = 0 # For camera position
        self.yDegrees = 0
        self.zDegrees = 0
        base.camera.setPos(0, -self.camDistance, 0)
        # Listen for events
        base.accept("wheel_up", self.zoomIn)
        base.accept("wheel_down", self.zoomOut)
        base.accept("mouse1", self.camControlOn)
        base.accept("mouse1-up", self.camControlOff)
        base.accept("window-resize", self.handleWindowResize)
        # Add camera/player control movement task to global task manager
        base.taskMgr.add(self.camControlTask, 'camControlTask')

    def handleWindowResize(self):
        # Change center x,y if window is resized
        bprops = base.win.getProperties()
        self.centerX  = bprops.getXSize() / 2
        self.centerY = bprops.getYSize() / 2

    def camControlOn(self):
        self.camControl = True
        self.props.setCursorHidden(True) 
        base.win.requestProperties(self.props)
        m = base.win.getPointer(0)
        self.storedMouseX = m.getX()
        self.storedMouseY = m.getY()
        base.win.movePointer(0, self.centerX, self.centerY)

    def camControlOff(self):
        self.camControl = False
        self.props.setCursorHidden(False)
        base.win.requestProperties(self.props)
        base.win.movePointer(0, int(self.storedMouseX),
                             int(self.storedMouseY))
        
    def zoomIn(self):
        self.camDistance = self.camDistance - self.zoomSpeed
        if self.camDistance < self.zoomMin:
            self.camDistance = self.zoomMin

    def zoomOut(self):
        self.camDistance = self.camDistance + self.zoomSpeed
        if self.camDistance > self.zoomMax:
            self.camDistance = self.zoomMax

    def camControlTask(self, task):
        if self.camControl:
            # If camControl is active, update position based on mouse
            m = base.win.getPointer(0)
            base.win.movePointer(0, self.centerX, self.centerY)
            # Change x and y based on horizontal mouse movement
            self.xDegrees = (self.xDegrees -
                             (m.getX() - self.centerX)) % 360
            # Change z based on vertical mouse movement
            self.yDegrees = (self.yDegrees - 
                             (m.getY() - self.centerY))
            # Limit height/min of cam
            if self.yDegrees >= 90:
                self.yDegrees = 90
            if self.yDegrees <= -90:
                self.yDegrees = -90
        # Update camera position and angle
        xRadians = self.radians(self.xDegrees)
        yRadians = self.radians(self.yDegrees)
        base.camera.setX(self.parent, self.camDistance * sin(xRadians))
        base.camera.setY(self.parent, -self.camDistance * cos(xRadians))
        base.camera.setZ(self.parent, -self.camDistance * sin(yRadians))
        base.camera.lookAt(self.parent)
        return task.cont

    def radians(self, degrees):
        return (degrees * (pi / 180.0))

app = MyApp()
app.run()
