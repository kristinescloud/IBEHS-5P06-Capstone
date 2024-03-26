

class CalculateDepth:
    def __init__(self):
        self.object_widths = {
            0: 45.72,
            1: 41.91,
            3: 78.74,
            5: 259.08,
            6: 305,
            7: 244,
            11: 76,
            13: 183,
            15: 46,
            16: 56,
            24: 33,
            25: 61,
            28: 35.5,
            32: 22,
            36: 81,
            37: 213,
            38: 30,
            56: 46,
            57: 213,
            58: 30.48,
            59: 152,
            60: 91,
            61: 51,
            62: 122,
            68: 56,
            69: 76,
            70: 30,
            72: 91,
            74: 25.4
        }
    def calculate_depth(self, objectclass, width_pixels):
        f = 0.21 #in cm
        width_true = self.object_widths.get(objectclass)
        depth = f*(width_true/(1.4*1e-4*width_pixels))
        return depth

if __name__ == "main":
    cd = CalculateDepth()
    print(cd.calculate_depth(0, 300))
