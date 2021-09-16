

import matplotlib.pyplot as plt

import matplotlib.animation as animation

from matplotlib.animation import FuncAnimation
















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

    data1 = []
    names = []
    fig, axes = plt.subplots(1, len(summary.keys()))
    for name in summary.keys():
        names.append(name)
        small_orbits = summary[name]['small']
        large_orbits = summary[name]['large']
        data = [len(small_orbits), len(large_orbits)]
        data1.append(data)
        small_orbits = []
        large_orbits = []
    for i in range(len(summary.keys())):
        if int(len(summary.keys())) == 1:
            axes.bar(['small', 'large'], data1[i], color=['green', 'red'])
            plt.suptitle(f'Entities that orbit {names}', color='blue')
        else:
            axes[i].bar(['small', 'large'], data1[i], color=['green', 'red'])
            axes[i].title.set_text(names[i])
            plt.suptitle(f'Entities that orbit {names}', color='blue')
    plt.show()








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



