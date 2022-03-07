import json


class SensorDataList(dict):

    def __init__(self, *b, **a):
        super(SensorDataList, self).__init__(*b, **a)
        super().__init__()
        self.sensor_list = super(SensorDataList, self).keys()

    def add_sensor(self, sensor_name, value):
        self.update({sensor_name: value})

    def get_json(self):
        return json.dumps(self)


