# This code is so you can run the samples without installing the package
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
#

testinfo = "s, t 1, s, t 2, s, t 3, s, t 4.1, s, t 4.2, s, q"
tags = "FadeOutBLTiles, StopGrid, CocosNode.grid.active"

import pyglet
import cocos
from cocos.director import director
from cocos.actions import *
from cocos.layer import *

class BackgroundLayer(cocos.layer.Layer):
    def __init__(self):
        super(BackgroundLayer, self).__init__()
        self.img = pyglet.resource.image('background_image.png')

    def draw( self ):
        glColor4ub(255, 255, 255, 255)
        glPushMatrix()
        self.transform()
        self.img.blit(0,0)
        glPopMatrix()

def main():
    print description
    director.init( resizable=True, fullscreen=False )
    main_scene = cocos.scene.Scene()
    main_scene.add( BackgroundLayer(), z=0 )
    
    def check_grid(self):
        assert self.grid.active == False

    e = FadeOutBLTiles( grid=(16,12), duration=2 )
    # a sequence of grid actions should terminate with the action StopGrid,
    # else the scene will continue to do a double render for each frame
    main_scene.do( e + Reverse(e) + StopGrid() + CallFuncS(check_grid))

    director.run (main_scene)

description = """
Demostrates the FadeOutBLTiles action and verifies that after StopGrid
self.grid.active == False
"""

if __name__ == '__main__':
    main()
