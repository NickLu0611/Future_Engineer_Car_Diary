class tools():        
    def constrain(self, x, out_min, out_max):
        return out_min if x < out_min else out_max if x > out_max else x

    def mapping(self, x, in_min, in_max, out_min, out_max):
        return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min
