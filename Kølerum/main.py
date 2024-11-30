'''This is the main file to run the simulation. 
It will call the main function from the Simulation file 
and plot the results if wanted'''


from Simulation import main
import matplotlib.pyplot as plt

# Number of iterations
iterations = 500


# Choose between 'smart' and 'simple'
thermostat = 'smart'

if __name__ == '__main__':
    y = main(iterations, thermostat)
    x = range(len(y))
    plt.plot(x, y)
    #plt.show()


