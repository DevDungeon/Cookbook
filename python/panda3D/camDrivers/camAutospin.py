from math import pi, sin, cos
 
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
 
        # Add the spinCameraTask procedure to the task manager.
        self.taskMgr.add(self.spinCameraTask, "SpinCameraTask")
 
    # Define a procedure to move the camera.
    def spinCameraTask(self, task):
        angleDegrees = task.time * 6.0
        angleRadians = angleDegrees * (pi / 180.0)
        camDistance = 20
        self.camera.setPos(camDistance * sin(angleRadians),
                           -camDistance * cos(angleRadians),
                           3)
        self.camera.setHpr(angleDegrees, .5, 0)
        return task.cont
 
app = MyApp()
app.run()
