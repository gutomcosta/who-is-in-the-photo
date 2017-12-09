class Face(object):
    def __init__(self, image, top, right, bottom, left):
        self.top = top
        self.right = right
        self.bottom = bottom
        self.left = left
        self.original_image = image

    
    def image(self):
        # top = self.top - 30 > self.ori
        
        return self.original_image[self.top-30:self.bottom+30, self.left-30:self.right+30]
        # return self.original_image[self.top:self.bottom, self.left:self.right]
        

