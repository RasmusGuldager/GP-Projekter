from Simulation import main
import matplotlib.pyplot as plt


iterations = 500


# Choose between 'smart' and 'simple'
thermostat = 'smart'

if __name__ == '__main__':
    y = main(iterations, thermostat)
    x = range(len(y))
    plt.plot(x, y)


