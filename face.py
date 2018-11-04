class Face:
    def __init__(self, obs):
        self.emotion = obs.get("emotion")
        self.usage = obs.get("Usage")
        self.image = obs.get("pixels")

    def emotion(self):
        return self.emotion

    def usage(self):
        return self.usage

    def image(self):
        return self.image