from numpy import random
import csv
import random
import copy
import time
"""
Algorithm that forces unique configurations on every turn. 
"""


def unique(inst, cars):
    start=time.time()
    # Copy of the main game instance
    instance_copy = copy.deepcopy(inst)

    movements = 0

    def save_board(instance_copy):
        # saves car coordinates of current move in a dictionary
        key = movements
        step = {instance_copy.cars[car]: (
            instance_copy.cars[car].col, instance_copy.cars[car].row) for car in instance_copy.cars}

        instance_copy.version[key] = step

        return instance_copy.version
    
    def empty_saves(instance_copy):
        instance_copy.version.clear()
        return instance_copy.version

    def check_move(instance_copy):
        # checks if move configuration has been achieved in earlier step and returns False if this is the case
        current = {instance_copy.cars[car]: (instance_copy.cars[car].col, instance_copy.cars[car].row) for car in instance_copy.cars}

        for board in instance_copy.version:
            if instance_copy.version[board] == current:
                return False

        return True


    # Run loop while game not winnable
    while not instance_copy.check_win():
        dupe=instance_copy
        # Choose a car randomly
        randomcar = random.choice(list(cars))

        # Check movable spaces of the car
        movementspace = instance_copy.check_space(randomcar)

        # Choose a move randomly
        randommovement = random.choice(movementspace)

        # Perform movement if this is possible
        if  dupe.move(randomcar, randommovement):
            if check_move(instance_copy):
                instance_copy.move(randomcar, randommovement)

                # Count movements made
                movements += 1

                # Reload board
                empty_board = instance_copy.create_board()
                instance_copy.load_board(empty_board)
                save_board(instance_copy)
            elif time.time()-start > 2:
                start=time.time()
                empty_saves(instance_copy)
                return unique(inst, cars)
            
            
    instance_copy.car_output()
    empty_saves(instance_copy)
    print(instance_copy.load_board(empty_board))
    return print(f"Oplossing met archief in {movements} steps.")
    

