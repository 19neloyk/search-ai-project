from game import Agent
from game import Directions
import random

class DumbAgent(Agent):
    "An agent that goes West until it can't."

    def getAction(self, state):
        "The agent receives a GameState (defined in pacman.py)."
        print("Location:", state.getPacmanPosition())
        print("Action available:", state.getLegalPacmanActions())
        if Directions.WEST in state.getLegalPacmanActions():
            print("Going West.")
            return Directions.WEST
        else:
            print("Stopping.")
            return Directions.STOP

class RandomAgent(Agent):
    "Based on the current options, the agent picks a random action to carry out."

    def getAction(self, state):
        "The agent receives a GameState"
        print("Location:", state.getPacmanPosition())
        print("Action available:", state.getLegalPacmanActions())
        choice = random.choice([i for i in state.getLegalPacmanActions() if i != Directions.STOP])
        print(choice)
        return choice

class ReflexAgent(Agent):
    """
    The agent looks at the possible legal actions, and if one of these actions would cause a food pellet to be
    eaten, it chooses that action. If none of the immediate actions lead to food, it chooses randomly
    from the possibilities (excluding 'Stop')
    """

    def getAction(self, state):
        print("Location:", state.getPacmanPosition())
        print("Action available:", state.getLegalPacmanActions())
        non_stop = [i for i in state.getLegalPacmanActions() if i != Directions.STOP]
        curr_food = state.getNumFood()
        for action in non_stop:
            next_state = state.generatePacmanSuccessor(action)
            if next_state.getNumFood() < curr_food:
                choice = action
                print("Eating food")
                break
        else:
            choice = random.choice(non_stop)
        print choice
        return choice
