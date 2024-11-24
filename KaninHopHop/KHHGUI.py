#This file imports the runGame() function from KaninHopHop.py.
#This file runs the runGame() function n times according to the userinput
#It also does all the GUI

#Importing all used libraries as well as the runGame function from the other python script
import PySimpleGUI as sg
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from KaninHopHop import runGame

#Function to draw the matplotlib figure on the PySimpleGUI canvas
def draw_figure(canvas, figure):
    figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack(side="top", fill="both", expand=1)
    return figure_canvas_agg

#Define the layout for the PySimpleGUI window
layout = [
    [sg.Text("Antal af spillere:")],
    [sg.InputText(key="numberOfPlayers")],
    [sg.Text("Regelsæt ift. slag af kanin: Normal (Default)")],
    [sg.Button("Langsom (fjern 1 kanin)", key="ruleSet_1"),
    sg.Button("Hurtig (slå igen)", key="ruleSet_2")],
    [sg.Text("Antal iterationer:")],
    [sg.InputText(key="iterations")],
    [sg.Button("Start Simulation"), sg.Button("Exit")],
    [sg.Canvas(key="canvas", size=(1000, 800))],
    [sg.Text("", key='-TEXT-', font=("Helvetica", 20))]
]

#Create the window with finalize=True to enable further customization
window = sg.Window("KaninHopHop Simulation", layout, finalize=True, resizable=True, element_justification='center')

ruleSet = 3

#Main event loop
while True:
    event, values = window.read()

    #Always listen for the event of a buttonclick
    if event == "ruleSet_1":
        ruleSet = 1
    elif event == "ruleSet_2":
        ruleSet = 2

    #If user closes window or clicks "Exit"
    if event == sg.WINDOW_CLOSED or event == "Exit":
        break

    #Start the simulation if "Start Simulation" is clicked
    if event == "Start Simulation":
        #Retrieve and convert input values from GUI
        try:
            numberOfPlayers = int(values["numberOfPlayers"])
            iterations = int(values["iterations"])
            
        except:
            sg.popup("Please enter valid integers for all inputs.")
            continue

        #Initialize winners dictionary
        winners = {f"player{i+1}": 0 for i in range(numberOfPlayers)}

        #Function to find the winner
        def findWinner(players):
            max_value = max(players.values())
            winner = [player for player, points in players.items() if points == max_value]
            for i in winner:
                winners[i] += 1

        #Set up data for plotting
        x = np.arange(1, iterations + 1, 1)
        y = [np.zeros(iterations) for i in range(numberOfPlayers)]

        #Update graph data
        def updateGraph(iteration):
            for player in range(len(winners.keys())):
                y[player][iteration - 1] = (winners[f"player{player + 1}"] / iteration) * 100

        #Run the simulation
        for i in range(iterations):
            findWinner(runGame(numberOfPlayers, ruleSet))
            updateGraph(i + 1)

        #Create the plot
        if iterations > 200:
            fig, ax = plt.subplots(figsize = (10, 8))
            for i in range(numberOfPlayers):
                ax.plot(x[150:], y[i][150:], label=f"Player {i+1}")
        else:
            fig, ax = plt.subplots(figsize = (10, 8))
            for i in range(numberOfPlayers):
                ax.plot(x, y[i], label=f"Player {i+1}")

        ax.set_xlabel("Iterations")
        ax.set_ylabel("Winning Percentage")
        ax.set_title("Winning Percentage Over Iterations")
        ax.legend(loc="upper left")

        #Create readable stats for user
        message = f"Chance of winning for the players:\n\n"
        for player, wins in winners.items():
            message += f"{player}: {wins} wins, with {round(wins/iterations * 100)}% chance of winning\n"
        window['-TEXT-'].update(message)

        #Draw the plot on the PySimpleGUI
        canvas_elem = window["canvas"]
        canvas = canvas_elem.TKCanvas
        draw_figure(canvas, fig)
        window.maximize()

window.close()