# Task 17: Import the modules csv, tui and visual
# TODO: Your code here
import csv
import tui
import visual



# Task 18: Create an empty list named 'records'.
# This will be used to store the date read from the source data file.
# TODO: Your code here
records= []


def run():
    # Task 19: Call the function welcome of the module tui.
    # This will display our welcome message when the program is executed.
    # TODO: Your code here
    tui.welcome()


    while True:
        # Task 20: Using the appropriate function in the module tui, display a menu of options
        # for the different operations that can be performed on the data.
        # Assign the selected option to a suitable local variable
        # TODO: Your code here
        option = tui.menu()




        # Task 21: Check if the user selected the option for loading data.  If so, then do the following:
        # - Use the appropriate function in the module tui to display a message to indicate that the data loading
        # operation has started.
        # - Load the data (see below).
        # - Use the appropriate function in the module tui to display a message to indicate that the data loading
        # operation has completed.
        #
        # To load the data, it is recommended that you create and call one or more separate functions that do the
        # following:
        # - Use the appropriate function in the module tui to retrieve a file path for the CSV data file.  You
        # should appropriately handle the case where this is None.
        # - Read each line from the CSV file and add it to the list 'records'. You should appropriately handle the case
        # where the file cannot be found
        # TODO: Your code here
        global records
        if option == 1:
            tui.started('Load Data')
            try:
                with open(tui.source_data_path(),'r') as csv_file:
                    reader = csv.reader(csv_file)
                    for temp_list in reader:
                        records.append(temp_list)
            except FileNotFoundError:
                print('Data file does not exist')
                print()
            print(records)

            tui.completed('Load Data')
            print()




        # Task 22: Check if the user selected the option for processing data.  If so, then do the following:
        # - Use the appropriate function in the module tui to display a message to indicate that the data processing
        # operation has started.
        # - Process the data (see below).
        # - Use the appropriate function in the module tui to display a message to indicate that the data processing
        # operation has completed.
        #
        # To process the data, it is recommended that you create and call one or more separate functions that do the
        # following:
        # - Use the appropriate function in the module tui to display a menu of options for processing the data.
        # - Check what option has been selected
        #
        #   - If the user selected the option to retrieve an entity then
        #       - Use the appropriate function in the module tui to indicate that the entity retrieval process
        #       has started.
        #       - Use the appropriate function in the module tui to retrieve the entity name
        #       - Find the record for the specified entity in records.  You should appropriately handle the case
        #       where the entity cannot be found.
        #       - Use the appropriate function in the module tui to list the entity
        #       - Use the appropriate function in the module tui to indicate that the entity retrieval process has
        #       completed.
        #
        #   - If the user selected the option to retrieve an entity's details then
        #       - Use the appropriate function in the module tui to indicate that the entity details retrieval
        #       process has started.
        #       - Use the appropriate function in the module tui to retrieve the entity details
        #       - Find the record for the specified entity details in records.  You should appropriately handle the
        #       case where the entity cannot be found.
        #       - Use the appropriate function in the module tui to list the entity
        #       - Use the appropriate function in the module tui to indicate that the entity details retrieval
        #       process has completed.
        #
        #   - If the user selected the option to categorise entities by their type then
        #       - Use the appropriate function in the module tui to indicate that the entity type categorisation
        #       process has started.
        #       - Iterate through each record in records and assemble a dictionary containing a list of planets
        #       and a list of non-planets.
        #       - Use the appropriate function in the module tui to list the categories.
        #       - Use the appropriate function in the module tui to indicate that the entity type categorisation
        #       process has completed.
        #
        #   - If the user selected the option to categorise entities by their gravity then
        #       - Use the appropriate function in the module tui to indicate that the categorisation by entity gravity
        #       process has started.
        #       - Use the appropriate function in the module tui to retrieve a gravity range
        #       - Iterate through each record in records and assemble a dictionary containing lists of entities
        #       grouped into low (below lower limit), medium and high (above upper limit) gravity categories.
        #       - Use the appropriate function in the module tui to list the categories.
        #       - Use the appropriate function in the module tui to indicate that the categorisation by entity gravity
        #       process has completed.
        #
        #   - If the user selected the option to generate an orbit summary then
        #       - Use the appropriate function in the module tui to indicate that the orbit summary process has
        #       started.
        #       - Use the appropriate function in the module tui to retrieve a list of orbited planets.
        #       - Iterate through each record in records and find entities that orbit a planet in the list of
        #       orbited planets.  Assemble the found entities into a nested dictionary such that each entity can be
        #       accessed as follows:
        #           name_of_dict[planet_orbited][category]
        #       where category is "small" if the mean radius of the entity is below 100 and "large" otherwise.
        #       - Use the appropriate function in the module tui to list the categories.
        #       - Use the appropriate function in the module tui to indicate that the orbit summary process has
        #       completed.
        # TODO: Your code here
        elif option == 2:
            tui.started('Process Data')
            option1 = tui.process_type()
            if option1 == 1:
                tui.started('Retrieve entity')
                name = tui.entity_name()
                temp_entity_list = [x[0] for x in records]
                if name in temp_entity_list:
                    for item_index in range(0, len(records)):
                        if name == records[item_index][0]:
                            tui.list_entity(entity=records[item_index],cols =[])#using function list_entity to print the entity details
                else:
                    Print('Entity not found')
                    continue
            elif option1 == 2:
                tui.started('Retrieve entity details')
                record = tui.entity_details()
                #print(record)
                tui.completed('Retrieve entity details')
            elif option1 == 3:
                tui.started('Categorise entities by type')
                planets = []
                nonplanets = []
                for sublist in records:
                    if sublist[1] == 'FALSE':
                        nonplanets.append(sublist[0])
                    elif sublist[1] == 'TRUE':
                        planets.append(sublist[0])
                my_dict = {'Planets': planets , 'Non-planets': nonplanets}





                tui.completed('Categorise entities by type')
            elif option1 == 4:
                tui.started('Categorise entities by gravity')
                gravity_range = tui.gravity_range()
                below_lower_limit = []
                above_upper_limit = []
                between_lower_and_upper = []
                records_minus_first_line = records[1:]
                for sublist_gravity in records_minus_first_line:
                    if float(sublist_gravity[8]) < float(gravity_range[0]):
                        below_lower_limit.append(sublist_gravity[0])
                    elif float(sublist_gravity[8]) > float(gravity_range[1]):
                        above_upper_limit.append(sublist_gravity[0])
                    else:
                        between_lower_and_upper.append(sublist_gravity[0])
                my_dict_gravity = {'Low': below_lower_limit, 'Medium': between_lower_and_upper, 'High': above_upper_limit}
                print(my_dict_gravity)

                tui.completed('Categorise entities by gravity')
            elif option1 == 5:
                tui.started('Summarise entities by orbit')

                tui.completed('Summarise entities by orbit')
            tui.completed('Process Data')






        # Task 23: Check if the user selected the option for visualising data.  If so, then do the following:
        # - Use the appropriate function in the module tui to indicate that the data visualisation operation
        # has started.
        # - Visualise the data (see below).
        # - Use the appropriate function in the module tui to display a message to indicate that the data visualisation
        # operation has completed.
        # To visualise the data, it is recommended that you create and call one or more separate functions that do the
        # following:
        # - Use the appropriate function in the module tui to retrieve the type of visualisation to display.
        # - Check what option has been selected
        #
        #   - if the user selected the option to visualise the entity type then
        #       - Use the appropriate function in the module tui to indicate that the entity type visualisation
        #       process has started.
        #       - Use your code from earlier to assemble a dictionary containing a list of planets and a list of
        #       non-planets.
        #       - Use the appropriate function in the module visual to display a pie chart for the number of planets
        #       and non-planets
        #       - Use the appropriate function in the module tui to indicate that the entity type visualisation
        #       process has completed.
        #
        #   - if the user selected the option to visualise the entity gravity then
        #       - Use the appropriate function in the module tui to indicate that the entity gravity visualisation
        #       process has started.
        #       - Use your code from earlier to assemble a dictionary containing lists of entities grouped into
        #       low (below lower limit), medium and high (above upper limit) gravity categories.
        #       - Use the appropriate function in the module visual to display a bar chart for the gravities
        #       - Use the appropriate function in the module tui to indicate that the entity gravity visualisation
        #       process has completed.
        #
        #   - if the user selected the option to visualise the orbit summary then
        #       - Use the appropriate function in the module tui to indicate that the orbit summary visualisation
        #       process has started.
        #       - Use your code from earlier to assemble a nested dictionary of orbiting planets.
        #       - Use the appropriate function in the module visual to display subplots for the orbits
        #       - Use the appropriate function in the module tui to indicate that the orbit summary visualisation
        #       process has completed.
        #
        #   - if the user selected the option to animate the planet gravities then
        #       - Use the appropriate function in the module tui to indicate that the gravity animation visualisation
        #       process has started.
        #       - Use your code from earlier to assemble a dictionary containing lists of entities grouped into
        #       low (below lower limit), medium and high (above upper limit) gravity categories.
        #       - Use the appropriate function in the module visual to animate the gravity.
        #       - Use the appropriate function in the module tui to indicate that the gravity animation visualisation
        #       process has completed.
        # TODO: Your code here
        elif option == 3:
            tui.started('Visualise Data')
            o = tui.visualise()
            if o == 1:
                tui.started('Entities by type')
                planets = []
                nonplanets = []
                for sublist in records:
                    if sublist[1] == 'FALSE':
                        nonplanets.append(sublist[0])
                    elif sublist[1] == 'TRUE':
                        planets.append(sublist[0])
                categories = {'Planets': planets, 'Non-Planets': nonplanets}

                visual.entities_pie(categories)
                tui.completed('Entities by type')
            elif o == 2:
                tui.started('Entities by gravity')
                gravity_range = tui.gravity_range()
                below_lower_limit = []
                above_upper_limit = []
                between_lower_and_upper = []
                records_minus_first_line = records[1:]
                for sublist_gravity in records_minus_first_line:
                    if float(sublist_gravity[8]) < float(gravity_range[0]):
                        below_lower_limit.append(sublist_gravity[0])
                    elif float(sublist_gravity[8]) > float(gravity_range[1]):
                        above_upper_limit.append(sublist_gravity[0])
                    else:
                        between_lower_and_upper.append(sublist_gravity[0])
                my_dict_gravity = {'Low': below_lower_limit, 'Medium': between_lower_and_upper,
                                   'High': above_upper_limit}
                visual.entities_bar()
                tui.completed('Entities by gravity')
            elif o == 3:
                tui.started('Summary of orbits')
#Use your code from earlier to assemble a nested dictionary of orbiting planets.
                visual.orbits()
                tui.completed('Summary of orbits')
            elif o == 4:
                tui.started('Animate gravities')
#    - Use your code from earlier to assemble a dictionary containing lists of entities grouped into
#       low (below lower limit), medium and high (above upper limit) gravity categories.
                visual.gravity_animation(  )
                tui.completed('Animate gravities')
            tui.completed('Visualise Data')

        # Task 28: Check if the user selected the option for saving data.  If so, then do the following:
        # - Use the appropriate function in the module tui to indicate that the save data operation has started.
        # - Save the data (see below)
        # - Use the appropriate function in the module tui to indicate that the save data operation has completed.
        #
        # To save the data, you should demonstrate the application of OOP principles including the concepts of
        # abstraction and inheritance.  You should create an AbstractWriter class with abstract methods and a concrete
        # Writer class that inherits from the AbstractWriter class.  You should then use this to write the records to
        # a JSON file using in the following order: all the planets in alphabetical order followed by non-planets 
        # in alphabetical order.
        # TODO: Your code here
        elif option == 4:
            tui.started('Save Data')


            tui.completed('Save Data')
        # Task 29: Check if the user selected the option for exiting.  If so, then do the following:
        # break out of the loop
        # TODO: Your code here
        elif option == 5:
            break
        # Task 30: If the user selected an invalid option then use the appropriate function of the module tui to
        # display an error message
        # TODO: Your code here
        else:
            tui.error('Invalid Option')


if __name__ == "__main__":

 run()

# C:\Users\maryus666\Desktop\QHO426\QHO426\data\sol_data.csv