import math

class simple_thermostat:
    def __init__(self):
        self.target_temp = 5

    def check_compressor(self, cooling_room_instance):
        if cooling_room_instance.temp > self.target_temp:
            cooling_room_instance.compressor = "on"
        else:
            cooling_room_instance.compressor = "off"

class smart_thermostat:
    def __init__(self, kwh_price):
        self.safe_temp_range_min = 5
        self.safe_temp_range_max = 6.3
        self.avg_price = sum(kwh_price) / len(kwh_price)


    def check_compressor(self, cooling_room_instance, kwh_price):
        if cooling_room_instance.temp <= self.safe_temp_range_min:
            cooling_room_instance.compressor = "off"
        elif cooling_room_instance.temp >= self.safe_temp_range_max:
            cooling_room_instance.compressor = "on"
        elif kwh_price < self.avg_price:
            cooling_room_instance.compressor = "on"
        else:
            cooling_room_instance.compressor = "off"
