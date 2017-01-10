import sys
import math

# Grab Snaffles and try to throw them through the opponent's goal!
# Move towards a Snaffle and use your team id to determine where you need to throw it.

my_team_id = int(input())  # if 0 you need to score on the right of the map, if 1 you need to score on the left

# Initiate lists for data storage
entity_idList=[]
entity_typeList=[]
xList=[]
yList=[]
vxList=[]
vyList=[]
stateList=[]

# class definitions
class WizardClass:
    """My wizards"""
    def __init__(self, x, y, vx, vy, state):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.state = state

class SnaffleClass:
    """My wizards"""
    def __init__(self, x, y, vx, vy, state):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.state = state

# game loop
while True:
    my_score, my_magic = [int(i) for i in input().split()]
    opponent_score, opponent_magic = [int(i) for i in input().split()]
    entities = int(input())  # number of entities still in game
    snaffleList=list() # list of ID's for the snaffles
    wizardList=list()           # list of ID's for my wizards

    for i in range(entities):
        # entity_id: entity identifier
        # entity_type: "WIZARD", "OPPONENT_WIZARD" or "SNAFFLE" (or "BLUDGER" after first league)
        # x: position
        # y: position
        # vx: velocity
        # vy: velocity
        # state: 1 if the wizard is holding a Snaffle, 0 otherwise
        entity_id, entity_type, x, y, vx, vy, state = input().split()

        if entity_type == "WIZARD"
            wizardList.add(WizardClass(x,y,vx,vy,state))

        elif entity_type == "SNAFFLE"
            snaffleID.add(i)

    for i in range(2):

        wizard=wizardList[i]

        # Write an action using print
        # To debug: print("Debug messages...", file=sys.stderr)


        # Edit this line to indicate the action for each wizard (0 ≤ thrust ≤ 150, 0 ≤ power ≤ 500)
        # i.e.: "MOVE x y thrust" or "THROW x y power"
        if state[wizardID[]]

        print("MOVE 8000 3750 100")
