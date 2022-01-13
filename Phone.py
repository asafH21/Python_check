from Student import Student


class Phone(Student):
    def __init__(self, screenSize, camera, numOfSpeakers, isSdCard):
        self.screenSize = screenSize
        self.camera = camera
        self.numOfSpeakers = numOfSpeakers
        self.isSdCard = isSdCard

    def screen(self):
        if self.screenSize > 6:
            return True
        else:
            return False
