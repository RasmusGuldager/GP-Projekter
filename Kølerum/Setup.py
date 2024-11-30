'''This module will setup classes for the cooling room and the price.'''


import numpy as np
import math
import doctest

class cooling_room:
    def __init__(self):
        self.temp = 5
        self.door = "closed"
        self.compressor = "off"
        self.room_temp = 20
        self.compressor_temp = -5
    
    def check_door(self):
        '''Simulates checking whether the door is open or closed.

        The door has a 10% chance of being open.

        >>> np.random.seed(0)
        >>> room = cooling_room()
        >>> room.check_door()
        >>> room.door
        'closed'

        >>> np.random.seed(6)
        >>> room.check_door()
        >>> room.door
        'open'
        '''

        if np.random.randint(1, 11) == 10:
            self.door = "open"
        else:
            self.door = "closed"
    
    def update_temp(self):
        '''Updates the temperature based on the door and compressor state.

        >>> room = cooling_room()
        >>> initial_temp = room.temp
        >>> room.check_door() 
        >>> room.update_temp()  # Updates the temp based on the door and compressor state
        >>> abs(room.temp - initial_temp) > 0
        True
        '''
        
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
        '''Updates the total price based on the cooling room's temperature and compressor state.

        >>> room = cooling_room()
        >>> p = price()
        >>> initial_price = p.total_price
        >>> room.temp = 2.5  # Below 3.5, price should increase
        >>> p.update_total_price(room, 0.15)
        >>> p.total_price > initial_price
        True

        >>> room.temp = 7  # Above 6.5, price should increase again
        >>> p.update_total_price(room, 0.20)
        >>> p.total_price > initial_price
        True
        '''

        # Price for food loss
        if cooling_room_instance.temp < 3.5:
            self.total_price += 4.39 * math.exp(-0.49 * cooling_room_instance.temp)
        elif cooling_room_instance.temp >= 6.5:
            self.total_price += 0.11 * math.exp(0.31 * cooling_room_instance.temp)

        # Price for compressor
        if cooling_room_instance.compressor == "on":
            self.total_price += kwh_price

if __name__ == '__main__':
    doctest.testmod()
    print('All tests passed')
