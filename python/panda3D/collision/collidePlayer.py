#import panda3d stuff
from direct.showbase.ShowBase import ShowBase
from panda3d.core import CollisionNode, CollisionSphere
from panda3d.core import CollisionHandlerFloor, CollisionTraverser
from panda3d.core import CollisionHandlerPusher, Point3
from direct.interval.IntervalGlobal import Sequence


class MyApp(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)

        # Create player node and attach camera and collision node/solid
        self.Player = render.attachNewNode('Player')
        self.camera.reparentTo(self.Player)
        self.PlayerCN = CollisionNode('Player')
        self.PlayerCNP = self.Player.attachNewNode(self.PlayerCN)
        self.PlayerCSph = CollisionSphere(0, 0, 0, 1)
        self.PlayerCN.addSolid(self.PlayerCSph)
        # Player collision sphere
        playerCS = CollisionSphere(0, 0, 0, 2)
        playerCNP = self.Player.attachNewNode(CollisionNode('cnode'))
        playerCNP.node().addSolid(playerCS)
        #PlayerCNP.reparentTo(self.camera)
        playerCNP.show() # This won't show since we are inside
        
        # Create generic sphere in the world in front of us to see
        self.Sphere = self.loader.loadModel("models/misc/sphere")
        self.Sphere.reparentTo(self.render)
        self.Sphere.setPos(0, 20, -0.2)
        # Collision sphere for visible sphere, slightly larger
        cs = CollisionSphere(0, 0, 0, 1)
        cnodePath = self.Sphere.attachNewNode(CollisionNode('cSpherenode'))
        cnodePath.node().addSolid(cs)
        cnodePath.show()
        
        # Create global collision traverser
        self.cTrav = CollisionTraverser()
        # Collision handler pusher - visible sphere will push back
        self.pusher = CollisionHandlerPusher()

        # Tell player sphere to act as pusher - or world object?
        self.cTrav.addCollider(cnodePath, self.pusher)
        self.pusher.addCollider(cnodePath, self.Sphere, base.drive.node())

        seq = self.Player.posInterval(5, Point3(0, 40, 0), 
                                     startPos=Point3(0, 0, 0), fluid=1).loop()

app = MyApp()
app.run()
