#!/bin/env python2
from panda3d.core import CollisionTraverser,CollisionNode
from panda3d.core import CollisionHandlerQueue,CollisionRay
from panda3d.core import BitMask32,CollisionSphere
from direct.showbase.ShowBase import ShowBase

"""
Notes -
- CollisionSolids are added to CollisionNodes, which are attached
to other nodes like player, enemy, camera
- CollisionTraverser is a collection of collisions added with
addCollider(node, handler)
- CollisionTraverser is run against a node, like render, and the
specified handler collects all the triggered colliders
- Tags can be added to collision nodes to pass useful info when collided
"""

class MyApp(ShowBase):
    
    def __init__(self):
        ShowBase.__init__(self)

        # Create a traverser and a handler
        self.cTrav = CollisionTraverser()
        self.cQueue = CollisionHandlerQueue()

        # Create the collision node that will store the collision
        # ray solid 
        self.pickerNode = CollisionNode('mouseRay')
        # Set bitmask for efficiency, only hit from objects with same mask
        self.pickerNode.setFromCollideMask(BitMask32.bit(1))
        # Attach collision node to camera, since that is the source
        self.pickerNP = camera.attachNewNode(self.pickerNode)

        # Add collision solid(ray) to collision node
        self.pickerRay = CollisionRay()
        self.pickerNode.addSolid(self.pickerRay)
        # Add collidable node(pickerNP) to the traverser
        # Collisions detected when traversed will go to cQueue
        self.cTrav.addCollider(self.pickerNP, self.cQueue)

        # Create visible sphere
        self.tmpSphere = self.loader.loadModel("models/misc/sphere")
        self.tmpSphere.reparentTo(self.render)
        self.tmpSphere.setColor(1, 1, 1, 1)
        self.tmpSphere.setPos(0, 100, 0)
        
        # Create collision sphere and attach to tmpSphere
        cSphere = CollisionSphere(0, 0, 0, 3)
        cnodePath = self.tmpSphere.attachNewNode(CollisionNode('cnode'))
        # Add collision solid(sphere) to collision node
        # Because tmpSphere/cSphere is child of render, which we traverse
        # later, it becomes a from collider automatically, we don't
        # need to addCollider since that is only for from collision nodes
        cnodePath.node().addSolid(cSphere)
        # Set bitmask to match the from collisionnode mask for efficiency
        cnodePath.setCollideMask(BitMask32.bit(1))
        # Show the collision sphere visibly, for debugging.
        cnodePath.show()
        # Set a custom tag on the collision node which becomes available
        # inside the collision event stored in the collision handler
        cnodePath.setTag('someTag', '1')

        # Add task to run every frame - set collision solid(ray)
        # to start at the current camera position, 
        self.mouseTask = taskMgr.add(self.mouseTask, 'mouseTask')

    def mouseTask(self, task):
        if self.mouseWatcherNode.hasMouse():
            mpos = base.mouseWatcherNode.getMouse()
            # Set collision ray to start at camera lens and endpoint at mouse
            self.pickerRay.setFromLens(base.camNode, mpos.getX(), mpos.getY())
            # Perform the collision traverse - follows the ray and logs
            # all collisions to the handler set earlier
            self.cTrav.traverse(self.render)
            # Get info from entries and use them
            if self.cQueue.getNumEntries() > 0:
                self.cQueue.sortEntries()
                print("Collision!")
                entry = self.cQueue.getEntry(0)
                print(entry)
                someTag = int(entry.getIntoNode().getTag('someTag'))
                print(someTag)
                # Collision detected, mouse must be over sphere
                self.tmpSphere.setColor(0,1,0,1)
            else:
                # No collisions, mouse is not over sphere, unset color
                # Not ideal to "unset" the color each frame
                self.tmpSphere.setColor(1,1,1,1)
        return task.cont

app = MyApp()
app.run()
