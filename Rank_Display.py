# By TryingToStudy, follow my twitch :)))))

from tkinter import *
import matplotlib.pyplot as plt
import csv

# variable, rank

f = open("RankDisplay.txt", "r")
data = f.read().split()
data = data[1]
ticks = data[1:3]
ticks = int(ticks)

f.close()

# store variable
initial_ticks = 0
final_ticks = 0
final_initial_difference = 0  # y axis


def ticks_initial():
    """Stores the initial value of ticks"""
    global initial_ticks
    initial_ticks += ticks


def win():
    """Defines win and updates the txt file for obs"""
    global ticks
    ticks += 1
    fl = open("RankDisplay.txt", 'w')
    
    # enter your rank here bellow!!!!! (example, diamond)
    fl.write(f'Grandmaster ({ticks}) LP')
    fl.close()


def loss():
    """Defines loss and updates the txt file for obs"""
    global ticks
    ticks -= 1
    fl = open("RankDisplay.txt", 'w')

    # enter your rank here bellow!!!!! (example, diamond)
    fl.write(f'Grandmaster ({ticks}) LP')
    fl.close()


def compdata():
    """takes the current data and gets the important values"""

    # store the final number of ticks
    global final_ticks
    final_ticks += ticks

    # get the final - initial ticks
    global final_initial_difference
    global initial_ticks
    final_initial_difference += (final_ticks - initial_ticks)


def call_button():
    """Calling the button into display"""
    window = Tk()

    button1 = Button(window, text="LP Up", command=win)
    button1.pack()

    button2 = Button(window, text="LP Down", command=loss)
    button2.pack()

    button3 = Button(window, text="End Stream", command=lambda: [compdata(), window.destroy()])
    button3.pack()

    window.mainloop()


def data_plug():
    """Going to take the data and plug it in the csv file"""
    # get the important data
    global final_initial_difference
    difference_arr = [final_initial_difference]
    # write into file
    fl = open("RankDisplay.csv", "a")
    writer = csv.writer(fl)
    writer.writerow(difference_arr)

    fl.close()
    print("Data Automatically Saved!")


def scatterplot():
    """Takes data and plots it for easy progress view"""

    fl = open("RankDisplay.csv", "r")
    dat = fl.read().split()
    dat = dat[1:]

    fl.close()

    # arrays to store values for graphing
    day = []       # x axis
    win_loss_values = []        # y axis

    # day count
    count = 0

    # to properly divide and set up the arrays
    for i in dat:
        win_loss_values.append(int(i))
        count += 1
        day.append(count)

    # plot em
    plt.scatter(day, win_loss_values)
    plt.plot(day, win_loss_values)

    # labels
    plt.xlabel("Stream Day Number")
    plt.ylabel("Win/Loss Difference")
    plt.title("LP Gained/Lost")

    plt.show()


# Run it :)
ticks_initial()
call_button()
data_plug()
scatterplot()
