# Copyright 2020 Google LLC. This software is provided as-is, without
#  warranty or representation for any use or purpose. Your use of it 
# is subject to your agreement with Google. 


class home_object:
    def __init__(self, name, score):
        self.name = name
        self.score = score
        self.location = None
        self.object_text = ""
    
    def update_location(self, vertex1, vertex4):
        """Create an x1, y1, x2, y2 rectangle using the normalized values supplied from vertex1 and vertex4 in the vision API. This result is normalized 0-1 based on image height and width."""
        x1 = vertex1.x
        y1 = vertex1.y
        x2 = vertex4.x
        y2 = vertex4.y
        self.location=(x1,y1,x2,y2)
        
class text_annotation:
    def __init__(self, text, image_height, image_width):
        self.text = text
        self.location = None
        self.original_image_height = image_height
        self.original_image_width = image_width
        
    def update_location(self, vertex1, vertex4):
        """Create an x1, y1, x2, y2 rectangle vertex1 and vertex4 in the text annotation result.  The input isn't normalized, so it will be normalized here."""
        x1 = vertex1.x / self.original_image_width
        y1 = vertex1.y / self.original_image_height
        x2 = vertex4.x / self.original_image_width
        y2 = vertex4.y / self.original_image_height
        self.location=(x1, y1, x2, y2)
        
