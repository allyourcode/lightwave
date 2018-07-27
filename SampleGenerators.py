class PanelGenerator:
    counter = 0 # Frame count so far

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def next_frame(self):
        return [width*height * (141, 58, 127)]

class SolidGenerator(PanelGenerator):
    def __init__(self, width, height, color):
        self.width = width
        self.height = height
        self.color = color
    def next_frame(self):
        return self.width*self.height * [self.color]

class SolidPulse(PanelGenerator):
    def __init__(self, width, height, color):
        self.width = width
        self.height = height
        self.color = color
        self.counter = min(color)
        self.direction = 0

    def next_frame(self):
        if self.counter <= 0:
            self.counter == 0
            self.direction = 1
        elif self.counter >= min(self.color):
            self.counter = min(self.color)
            self.direction = 0
        if self.direction:
            self.counter = self.counter + 1
        else:
            self.counter = self.counter -1

        # Modify our colors
        r = self.color[0] - self.counter
        g = self.color[1] - self.counter
        b = self.color[2] - self.counter

        print(self.counter)

        return self.width*self.height *[(r,g,b)]
