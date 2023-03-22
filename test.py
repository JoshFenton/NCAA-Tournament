class test:
    def __init__(self, name=None, to=None, fro=None):
        self.to = to
        self.fro = fro
        self.name = name
    
    def connect_to(self, dest):
        self.to = dest
        self.to.fro = self