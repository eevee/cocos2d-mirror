# This code is so you can run the samples without installing the package
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
#


import cocos
from cocos.director import director
from cocos.sprite import Sprite
from cocos.actions import Place, MoveBy, Reverse

import pyglet

class TestLayer(cocos.layer.Layer):
    def __init__(self):
        super( TestLayer, self ).__init__()
        
        x,y = director.get_window_size()
        
        self.sprite = Sprite( 'grossini.png', (x/2,y/2)  )
        self.add( self.sprite )
        self.sprite2 = Sprite( 'grossini.png', (x/2,y/2)  )
        self.add( self.sprite2 )
        
        seq = MoveBy( (x/2, 0) ) + MoveBy( (0,y/2) )
        self.sprite.do( seq )
        self.sprite2.do( Reverse( seq ) )
        
        

if __name__ == "__main__":
    print "starting from midscreen, sprite 1 moves left and then up;"
    print "sprite2 does the reverse action "
    director.init()
    test_layer = TestLayer ()
    main_scene = cocos.scene.Scene (test_layer)
    director.run (main_scene)
