# This code is so you can run the samples without installing the package
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
#


import cocos
from cocos.director import director
from cocos.sprite import ActionSprite
import pyglet

class TestLayer(cocos.layer.Layer):
    def __init__(self):
        super( TestLayer, self ).__init__()
        
        x,y = director.get_window_size()
        
        self.batch = cocos.sprite.BatchNode()
        self.add( self.batch )
        
        self.sprite = ActionSprite('grossini.png')
        self.sprite.position = x/2, y/2

        self.sprite2 = ActionSprite('grossini.png')
        self.sprite2.position = 20, 30

        self.sprite5 = ActionSprite('grossini.png')
        self.sprite5.position = -20, 30

        self.sprite3 = ActionSprite('grossini.png')
        self.sprite3.position = -20, -30
        
        self.sprite4 = ActionSprite('grossini.png')
        self.sprite4.position = 20, -30
        
        self.sprite.add( self.sprite2, z=-1 )
        self.sprite3.add( self.sprite4, z=1 )
        self.batch.add( self.sprite  )
        self.sprite.add( self.sprite3, z=-1 ) 
        self.sprite2.add( self.sprite5, z=1 )       
        

if __name__ == "__main__":
    director.init()
    test_layer = TestLayer ()
    main_scene = cocos.scene.Scene (test_layer)
    director.run (main_scene)
