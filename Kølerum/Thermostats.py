class simple_thermostat:
    def __init__(self):
        self.target_temp = 5

    def check_compressor(self, cooling_room_instance):
        if cooling_room_instance.temp > self.target_temp:
            cooling_room_instance.compressor = "on"
        else:
            cooling_room_instance.compressor = "off"

class smart_thermostat:
    def __init__(self):
        self.target_temp = 6.4

    def check_compressor(self, cooling_room_instance):
        if cooling_room_instance.temp > self.target_temp:
            cooling_room_instance.compressor = "on"
        else:
            cooling_room_instance.compressor = "off"