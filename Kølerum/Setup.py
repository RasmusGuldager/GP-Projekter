import numpy as np
import math


class cooling_room:
    def __init__(self):
        self.temp = 5
        self.door = "closed"
        self.compressor = "off"
        self.room_temp = 20
        self.compressor_temp = -5
    
    def check_door(self):
        if np.random.randint(1, 11) == 10:
            self.door = "open"
        else:
            self.door = "closed"
    
    def update_temp(self):
        if self.door == "closed" and self.compressor == "off":
            self.temp += 5 * 10**-7 * (self.room_temp - self.temp) * 300
        elif self.door == "open" and self.compressor == "off":
            self.temp += 3 * 10**-5 * (self.room_temp - self.temp) * 300
        elif self.door == "closed" and self.compressor == "on":
            self.temp += (5 * 10**-7 * (self.room_temp - self.temp) + 8 * 10**-6 * (self.compressor_temp - self.temp)) * 300
        else:
            self.temp += (3 * 10**-5 * (self.room_temp - self.temp) + 8 * 10**-6 * (self.compressor_temp - self.temp)) * 300


            
class price:
    def __init__(self):
        self.total_price = 0


    def update_total_price(self, cooling_room_instance, kwh_price):
        # Price for food loss
        if cooling_room_instance.temp < 3.5:
            self.total_price += 4.39 * math.exp(-0.49 * cooling_room_instance.temp)
        elif cooling_room_instance.temp >= 6.5:
            self.total_price += 0.11 * math.exp(0.31 * cooling_room_instance.temp)

        # Price for compressor
        if cooling_room_instance.compressor == "on":
            self.total_price += kwh_price