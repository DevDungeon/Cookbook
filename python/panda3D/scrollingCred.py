from pandac.PandaModules import * 
from direct.showbase.DirectObject import DirectObject 
from direct.gui.DirectGui import * 
import direct.directbase.DirectStart 
import sys, string, math 

globalClock.setMode(ClockObject.MSlave) 

def cycleAlpha(): 
    global VARIANT 
    VARIANT=(VARIANT+1)%len(images) 
    tex.load(images[VARIANT]) 

VARIANT=0 
images=[] 

#_____TOP & BOTTOM FADE 
img=PNMImage(32,32) 
img.addAlpha() 
img.fill(1) 
img.alphaFill(1) 
for x in range(img.getXSize()): 
    for y in range(img.getYSize()): 
        img.setAlpha(x,y,-.2+2.5*math.sin(math.pi*y/img.getYSize())) 
images.append(img) 
#_____SPOTLIGHT 
img=PNMImage(32,32) 
img.addAlpha() 
img.renderSpot(Vec4D(1,1,1,1),Vec4D(1,1,1,0),.6,1) 
images.append(img) 
#_____DOUGHNUT o_0 
img1=PNMImage() 
img1.copyFrom(img) 
img2=PNMImage(32,32) 
img2.addAlpha() 
img2.renderSpot(Vec4D(1,1,1,0),Vec4D(1,1,1,1),.1,.4) 
img1.darkenSubImage(img2,0,0,0,0) 
images.append(img1) 

tex=Texture() 
tex.load(images[VARIANT]) 
tex.setWrapU(Texture.WMClamp) 
tex.setWrapV(Texture.WMClamp) 


# background 
osi=OnscreenImage('maps/4map.rgb',parent=render2d) 
osi.setColor(.2,.2,.2,1) 

# alpha preview 
CM=CardMaker('') 
card=base.a2dBottomLeft.attachNewNode(CM.generate()) 
card.setScale(.25) 
card.setTexture(tex) 
card.setTransparency(1) 
ost=OnscreenText(parent=base.a2dBottomLeft, font=loader.loadFont('cmss12'), 
   text='press\nSPACE\nto cycle', fg=(0,0,0,1),shadow=(1,1,1,1), scale=.045) 
NodePath(ost).setPos(card.getBounds().getCenter()-ost.getBounds().getCenter()) 

dummyParent=NodePath('') 
textParent=dummyParent.attachNewNode('') 
textParent.setDepthTest(0) 
textParent.setDepthWrite(0) 

# THE CREDITS TEXT 
ost = OnscreenText(parent=textParent, font=loader.loadFont('cmss12'), 
   text='CREDITS\n\n'+'\n'.join([c*30 for c in string.ascii_letters]), 
   fg=(1,1,1,1),scale=.065) 
ost.setP(-90) 
ost.flattenLight() 

ts=TextureStage('') 
textParent.setTexGen(ts,TexGenAttrib.MWorldPosition) 
textParent.setTexScale(ts,.5,.5) 
textParent.setTexOffset(ts,.5,.5) 
textParent.setTexture(ts,tex) 
b3=textParent.getTightBounds() 
dims=b3[1]-b3[0] 
textParent.posInterval(50,Point3(0,dims[1]+2,0),Point3(0,-1.05,0)).start() 

VPcam = Camera('vpcam') 
VPcam.copyLens(base.cam2d.node().getLens()) 
VPcamNP = dummyParent.attachNewNode(VPcam) 
VPcamNP.setP(-90) 
dr=base.win.makeDisplayRegion() 
dr.setCamera(VPcamNP) 
dr.setSort(1000) 


do=DirectObject() 
do.accept('space',cycleAlpha) 
do.accept('escape',sys.exit) 
globalClock.setMode(ClockObject.MNormal) 
run()