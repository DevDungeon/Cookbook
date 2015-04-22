from math import pi, sin, cos
from direct.gui.DirectGui import *
from direct.showbase.ShowBase import ShowBase
from direct.task import Task
from direct.actor.Actor import Actor
 
class MyApp(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
    
        # Frame in the bottom left
        myFrame = DirectFrame(frameColor=(0, 0, 0.65, 1),
                      frameSize=(-1, 1, -1, 1))
        myFrame.setPos(-0.5, 0, -0.5)

        # Button Example
        b = DirectButton(text = ("OK", "clicking", "rolling over", "disabled"))

    #def showValue():
    #    print slider['value']
    
    #slider = DirectSlider(range=(0,100), value=50, pageSize=3, command=showValue)

 
app = MyApp()
app.run()
