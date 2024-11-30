from Simulation import main
import matplotlib.pyplot as plt
import matplotlib

matplotlib.use('TkAgg')

iterations = 200


# Choose between 'smart' and 'simple'
thermostat = 'smart'

if __name__ == '__main__':
    y = main(iterations, thermostat)
    x = range(len(y))
    plt.plot(x, y)
    plt.show()


