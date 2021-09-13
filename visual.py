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

    plt.bar(['Low', 'Medium', 'High'], data, color=[ 'cyan', 'green', 'red'])
    plt.title('Entities by gravity', color = 'blue')
    plt.xlabel('Gravity type', color = 'blue')
    plt.ylabel('Number of entities', color = 'blue')
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

    for name in summary.keys():
        small_orbits = [item['small'] for item in summary.values()]
        large_orbits = [item['large'] for item in summary.values()]
        if small_orbits[0] == []:
            small_orbits.clear()
        if large_orbits[0] == []: #here if the planet to be orbited doesn't have any small or large orbits the result was an empty list inside another emty list and the len of this would have been 1
            large_orbits.clear()
        data = [len(small_orbits), len(large_orbits)]
        i = 1
        while i <= len(summary.keys()):
            plt.subplots(1,i)
            plt.bar(['small', 'large'], data, color=['green', 'red'])
            plt.title('Entities that orbit ' + str(name), color='blue')
            plt.xlabel('Orbit type', color='blue')
            plt.ylabel('Number of orbits', color='blue')
            plt.show()
            i += 1
            data= []



    #for planet_orbited, orbit_size in summary.items():
        #for key in orbit_size:
            #print(len(orbit_size[key]))






def gravity_animation(categories):

    """
    Task 27: Display an animation of "low", "medium" and "high" gravities.

    The function should display a suitable animation for the "low", "medium" and "high" gravity entities.
    E.g. an animated line plot

    :param categories: A dictionary containing "low", "medium" and "high" gravity entities
    :return: Does not return anything
    """
    fig = plt.figure(figsize=(8, 6))
    axes = fig.add_subplot(1, 1, 1)
    axes.set_ylim(0, 266)
    plt.style.use("seaborn")
    lst1 = [0, ((len(categories['Low']))/4), ((len(categories['Low']))/2), (3*(len(categories['Low']))/4), (len(categories['Low']))]
    lst2 = [0, ((len(categories['Medium']))/4), ((len(categories['Medium']))/2), (3*(len(categories['Medium']))/4), (len(categories['Medium']))]
    lst3 = [0, ((len(categories['High']))/4), ((len(categories['High']))/2), (3*(len(categories['High']))/4), (len(categories['High']))]
    y1 = []
    y2 = []
    y3 = []
    def animate(i):
        if i <= 4: # without this if statement i wqs getting an error index out of range.
            y1 = lst1[i]
            y2 = lst2[i]
            y3 = lst3[i]
            plt.bar(["Low", "Medium", "High"], [y1, y2, y3], color=[ 'cyan', 'green', 'red'])
    plt.title("Entities by gravity animation", color= 'blue')
    plt.xlabel('Gravity type' , color = 'blue')
    plt.ylabel('Number of entities', color = 'blue')
    ani = FuncAnimation(fig, animate)
    plt.show()



