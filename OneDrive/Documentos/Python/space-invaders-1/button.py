from PPlay.sprite import Sprite

class Button:
    def __init__(self, width, height, image):
        self.width = width
        self.height = height
        self.image = image
        self.sprite = Sprite(image)

    
