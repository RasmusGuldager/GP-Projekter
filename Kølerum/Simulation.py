import pandas as pd
import math
import numpy as np
from Setup import cooling_room, price
from Thermostats import smart_thermostat, simple_thermostat


def main(iterations, thermostat_type):
    kwh_price = pd.read_csv('elpris.csv')['Pris']
    total_cost = 0

    history = np.zeros(iterations)

    for i in range(iterations):
        cooling_room_instance = cooling_room()
        cost = price()
        if thermostat_type == 'simple':
            termostat = simple_thermostat()
        else:  
            termostat = smart_thermostat()

        for j in range(8640):
            cooling_room_instance.check_door()
            termostat.check_compressor(cooling_room_instance)
            cooling_room_instance.update_temp()
            cost.update_total_price(cooling_room_instance, kwh_price[j])
        
        total_cost += cost.total_price
        history[i] = cost.total_price
    

    avg_cost = total_cost / iterations

    print(f"Avg cost pr month is {math.floor(avg_cost)} DKK\n" + f"Calculated on {iterations} iterations")
    #print(f"{min(history)}, {history.index(min(history))}")
    return history

if __name__ == '__main__':
    main()
