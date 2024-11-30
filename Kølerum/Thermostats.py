import math
import numpy as np

class simple_thermostat:
    def __init__(self):
        self.target_temp = 5

    def check_compressor(self, cooling_room_instance):
        if cooling_room_instance.temp > self.target_temp:
            cooling_room_instance.compressor = "on"
        else:
            cooling_room_instance.compressor = "off"

class smart_thermostat:
    def __init__(self, kwh_prices):
        self.absolute_min_temp = 4
        self.safe_temp_range_min = 5.2
        self.safe_temp_range_max = 6.25
        self.avg_price = sum(kwh_prices) / len(kwh_prices)
        self.low_price = self.avg_price * 0.6


    def check_compressor(self, cooling_room_instance, kwh_price):
        if cooling_room_instance.temp > self.absolute_min_temp and kwh_price < self.low_price:
            cooling_room_instance.compressor = "on"
        elif cooling_room_instance.temp <= self.safe_temp_range_min:
            cooling_room_instance.compressor = "off"
        elif cooling_room_instance.temp >= self.safe_temp_range_max or kwh_price < self.avg_price:
            cooling_room_instance.compressor = "on"
        else:
            cooling_room_instance.compressor = "off"


