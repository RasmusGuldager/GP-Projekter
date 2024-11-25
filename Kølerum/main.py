import numpy as np
import math
import pandas as pd

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



class simple_termostat:
    def __init__(self):
        self.target_temp = 5

    def check_compressor(self, cooling_room_instance):
        if cooling_room_instance.temp > self.target_temp:
            cooling_room_instance.compressor = "on"
        else:
            cooling_room_instance.compressor = "off"

class smart_termostat:
    def __init__(self):
        self.target_temp = 0

    def check_compressor(self, cooling_room_instance):
        if cooling_room_instance.temp > self.target_temp:
            cooling_room_instance.compressor = "on"
        else:
            cooling_room_instance.compressor = "off"


def Main():
    kwh_price = pd.read_csv('elpris.csv')['Pris']
    total_cost = 0

    iterations = 1000

    for i in range(iterations):
        cooling_room_instance = cooling_room()
        cost = price()
        termostat = simple_termostat()

        for j in range(8640):
            cooling_room_instance.check_door()
            termostat.check_compressor(cooling_room_instance)
            cooling_room_instance.update_temp()
            cost.update_total_price(cooling_room_instance, kwh_price[j])
        
        total_cost += cost.total_price
    

    avg_cost = total_cost / iterations

    print(f"Avg cost pr month is {math.floor(avg_cost)} DKK\n" + f"Calculated on {iterations} iterations")


if __name__ == '__main__':
    Main()

