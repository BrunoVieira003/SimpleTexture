import os
import json

class GenericDatabase:
    def __init__(self, file_path):
        self.path = os.path.join(os.getcwd(), file_path)
        self.update()
    
    def update(self):
        with open(self.path, "r") as file:
            self.data = json.load(file)
    
    def set(self, name, value):
        if self.data.get(name):
            self.data[name] = value

        with open(self.path, "w") as file:
            file.write(json.dumps(self.data))
    
    def get(self, name):
        return self.data.get(name)
        