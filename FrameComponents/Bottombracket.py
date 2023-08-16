class Bottombracket:
    
    def __init__(self, scale = 1.0, r_out = 22, r_in = 19):
        self.r_out = r_out
        self.r_in = r_in
        self.scale = scale
        
    def points_bb_outline(self, offset = (500,500)):
        #bb shell outer outline
        x0 = offset[0] - self.r_out * self.scale
        y0 = offset[1] + self.r_out * self.scale
        x1 = offset[0] + self.r_out * self.scale
        y1 = offset[1] - self.r_out * self.scale
        
        #bb shell inner bore outline
        x2 = offset[0] - self.r_in * self.scale
        y2 = offset[1] + self.r_in * self.scale
        x3 = offset[0] + self.r_in * self.scale
        y3 = offset[1] - self.r_in * self.scale
        return ((x0, y0, x1, y1), (x2, y2, x3, y3))
    
    def points_bb_centerline(self, offset_x = 0, offset_y = 0):
        return (offset_x, offset_y)