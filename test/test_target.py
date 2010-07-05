# This code is so you can run the samples without installing the package
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
#


import cocos
from cocos.director import director
from cocos.sprite import Sprite
from cocos.actions import *
import pyglet

class Dummy:
    rotation = 0
    
    def __setattr__(self, attr, value):
        print "set", attr, "to", value    
    
class TestLayer(cocos.layer.Layer):
    def __init__(self):
        super( TestLayer, self ).__init__()
        
        x,y = director.get_window_size()
        
        self.sprite = Sprite('grossini.png')
        self.sprite.position = x/2, y/2
        self.add( self.sprite  )
        
        self.sprite.do( Rotate(90, 3), Dummy() )
        

if __name__ == "__main__":
    print "two actions at the same time" 
    director.init()
    test_layer = TestLayer ()
    main_scene = cocos.scene.Scene (test_layer)
    director.run (main_scene)
