from direct.showbase.ShowBase import ShowBase
from direct.showbase.DirectObject import DirectObject
from direct.interval.IntervalGlobal import Sequence, Func, Wait
from panda3d.core import CollisionTraverser, CollisionHandlerEvent
from panda3d.core import CollisionNode, CollisionSphere
from panda3d.core import VBase4
 
 
class World(DirectObject):
 
    def __init__( self ):
        # Initialize the traverser.
        base.cTrav = CollisionTraverser()
 
        # Initialize the handler.
        self.collHandEvent = CollisionHandlerEvent()
        self.collHandEvent.addInPattern('into-%in')
        self.collHandEvent.addOutPattern('outof-%in')
 
        # Make a variable to store the unique collision string count.
        self.collCount = 0
 
        # Load a model. Reparent it to the camera so we can move it.
        s = loader.loadModel('smiley')	
        s.reparentTo(camera)
        s.setPos(0, 25, 0)
 
        # Setup a collision solid for this model.
        sColl = self.initCollisionSphere(s, True)
 
        # Add this object to the traverser.
        base.cTrav.addCollider(sColl[0], self.collHandEvent)
 
        # Accept the events sent by the collisions.
        self.accept('into-' + sColl[1], self.collide3)
        self.accept('outof-' + sColl[1], self.collide4)
        print(sColl[1])
 
        # Load another model.
        t = loader.loadModel('smiley')
        t.reparentTo(render)
        t.setPos(5, 25, 0)
 
        # Setup a collision solid for this model.
        tColl = self.initCollisionSphere(t, True)
 
        # Add this object to the traverser.
        base.cTrav.addCollider(tColl[0], self.collHandEvent)
 
        # Accept the events sent by the collisions.
        self.accept('into-' + tColl[1], self.collide)
        self.accept('outof-' + tColl[1], self.collide2)
        print(tColl[1])
 
        print("WERT")
 
    def collide(self, collEntry):
        print("WERT: object has collided into another object")
        Sequence(Func(collEntry.getFromNodePath().getParent().setColor,
                      VBase4(1, 0, 0, 1)),
                 Wait(0.2),
                 Func(collEntry.getFromNodePath().getParent().setColor,
                      VBase4(0, 1, 0, 1)),
                 Wait(0.2),
                 Func(collEntry.getFromNodePath().getParent().setColor,
                      VBase4(1, 1, 1, 1))).start()
 
 
    def collide2(self, collEntry):
        print("WERT.: object is no longer colliding with another object")
 
    def collide3(self, collEntry):
        print("WERT2: object has collided into another object")
 
    def collide4(self, collEntry):
        print("WERT2: object is no longer colliding with another object")
 
    def initCollisionSphere(self, obj, show=False):
        # Get the size of the object for the collision sphere.
        bounds = obj.getChild(0).getBounds()
        center = bounds.getCenter()
        radius = bounds.getRadius() * 1.1
 
        # Create a collision sphere and name it something understandable.
        collSphereStr = 'CollisionHull' + str(self.collCount) + "_" + obj.getName()
        self.collCount += 1
        cNode = CollisionNode(collSphereStr)
        cNode.addSolid(CollisionSphere(center, radius))
 
        cNodepath = obj.attachNewNode(cNode)
        if show:
            cNodepath.show()
 
        # Return a tuple with the collision node and its corrsponding string so
        # that the bitmask can be set.
        return (cNodepath, collSphereStr)
 
ShowBase()
# Run the world. Move around with the mouse to create collisions.
w = World()
run()