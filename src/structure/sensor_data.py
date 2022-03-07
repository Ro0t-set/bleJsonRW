import json


class SensorData:
    def __init__(self, name, value):
        self.value = value
        self.name = name

    def get_json(self):
        return json.dumps({self.name + ":" + self.value})





