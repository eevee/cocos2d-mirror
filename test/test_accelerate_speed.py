# This code is so you can run the samples without installing the package
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
#


import cocos
from cocos.director import director
from cocos.actions import ActionSprite, Accelerate, Speed, Rotate
import pyglet

class TestLayer(cocos.layer.Layer):
    def __init__(self):
        super( TestLayer, self ).__init__()
        
        x,y = director.get_window_size()
        
        self.image = pyglet.resource.image('grossini.png')
        self.image.anchor_x = self.image.width / 2
        self.image.anchor_y = self.image.height / 2

        self.sprite1 = ActionSprite( self.image )
        self.add( self.sprite1, (x/4, y/2) )
        self.sprite2 = ActionSprite( self.image )
        self.add( self.sprite2, ((x/4)*3, y/2) )

        self.sprite1.do( Accelerate( Speed( Rotate( 360, 1 ), 0.1 ), 4)  )
        self.sprite2.do( Speed( Accelerate( Rotate( 360, 1 ), 4 ), 0.1)  )
        

if __name__ == "__main__":
    director.init()
    test_layer = TestLayer ()
    main_scene = cocos.scene.Scene (test_layer)
    director.run (main_scene)
