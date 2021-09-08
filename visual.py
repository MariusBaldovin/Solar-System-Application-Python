import random

import matplotlib.pyplot as plt

import matplotlib.animation as animation

from matplotlib.animation import FuncAnimation

import random














def entities_pie(categories):
    """
    Task 24: Display a single subplot that shows a pie chart for categories.

    The function should display a pie chart with the number of planets and the number of non-planets from categories.

    :param categories: A dictionary with planets and non-planets
    :return: Does not return anything
    """

    sizes = [len(categories['Planets']), len(categories['Non-Planets'])]
    labels = ['Planets', 'Non-Planets']
    plt.pie(sizes, labels=labels)
    plt.legend(title = 'Entities by type')
    plt.show()


def entities_bar(categories):

    """
    Task 25: Display a single subplot that shows a bar chart for categories.

    The function should display a bar chart for the number of 'low', 'medium' and 'high' gravity entities.

    :param categories: A dictionary with entities categorised into 'low', 'medium' and 'high' gravity
    :return: Does not return anything
    """
    data = [len(categories['Low']), len(categories['Medium']), len(categories['High'])]

    plt.bar(['Low', 'Medium', 'High'], data)
    plt.title('Entities by gravity')
    plt.xlabel('Gravity type')
    plt.ylabel('Number of entities')
    plt.show()


def orbits(summary):

      """
        Task 26: Display subplots where each subplot shows the "small" and "large" entities that orbit the planet.

        Summary is a nested dictionary of the form:
        summary = {
            "orbited planet": {
                "small": [entity, entity, entity],
                "large": [entity, entity]
            }
        }

        The function should display for each orbited planet in summary. Each subplot should show a bar chart with the
        number of "small" and "large" orbiting entities.

        :param summary: A dictionary containing the "small" and "large" entities for each orbited planet.
        :return: Does not return anything
        """


    #plt.show()

    #data = [len(summary.values()) , len(summary.values())]
    #plt.bar(['small', 'large'], data)



def gravity_animation(categories):

    """
    Task 27: Display an animation of "low", "medium" and "high" gravities.

    The function should display a suitable animation for the "low", "medium" and "high" gravity entities.
    E.g. an animated line plot

    :param categories: A dictionary containing "low", "medium" and "high" gravity entities
    :return: Does not return anything
    """
    """
    #fig = plt.figure(figsize=(8, 6))
    #axes = fig.add_subplot(1, 1, 1)
    fig, axes = plt.subplots()
    axes.set_ylim(0, 266)
    axes.set_xlim('low', 'medium', 'large')
    line, = axes.plot(0,0)
    x_data = []
    def animate(i):
       x_data.append(i + int(len(categories['low'])))
       x_data.append(i + int(len(categories['medium'])))
       x_data.append(i + int(len(categories['large'])))
       line.set_xdata(x_data)
       #plt.bar(['low', 'medium', 'large'], [l1, l2, l3])
    #plt.title('Entities by gravity animation')
    ani = FuncAnimation(fig = fig, func = animate, interval = 100)
    plt.show()
    """
    fig = plt.figure(figsize=(8, 6))
    axes = fig.add_subplot(1, 1, 1)
    axes.set_ylim(0, 266)
    plt.style.use("seaborn")
    lst1 = [0, ((len(categories['Low']))/4), ((len(categories['Low']))/2), (3*(len(categories['Low']))/4), (len(categories['Low']))]
    lst2 = [0, ((len(categories['Medium']))/4), ((len(categories['Medium']))/2), (3*(len(categories['Medium']))/4), (len(categories['Medium']))]
    lst3 = [0, ((len(categories['High']))/4), ((len(categories['High']))/2), (3*(len(categories['High']))/4), (len(categories['High']))]
    y1 = [ ]
    y2 = [ ]
    y3 = [ ]
    def animate(i):
        y1 = lst1[i]
        y2 = lst2[i]
        y3 = lst3[i]
        plt.bar(["Low", "Medium", "High"], [y1, y2, y3])
    plt.title("Entities by gravity animation")
    ani = FuncAnimation(fig, animate)



    plt.show()



