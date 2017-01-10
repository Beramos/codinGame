import sys
import math

# Grab Snaffles and try to throw them through the opponent's goal!
# Move towards a Snaffle and use your team id to determine where you need to throw it.

my_team_id = int(input())  # if 0 you need to score on the right of the map, if 1 you need to score on the left

# initiate center of goals
if my_team_id is 1:
    goalCenter=(0, 3750)
else:
    goalCenter=(16000, 3750)

# initiate lists for data storage
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

    def findMyClosestSnaffleLocation(self,SnaffleList,numberOfSnaffles):
        distance=10**7
        for i in range(numberOfSnaffles): #find closest Snaffle
            distanceTemp=math.sqrt((SnaffleList[i].x-self.x)**2+(SnaffleList[i].y-self.y)**2) #calculate euclidean distance
            if distanceTemp < distance: #keep minimum distance and store location
                distance = distanceTemp
                location=(SnaffleList[i].x, SnaffleList[i].y)

        return(location)

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
    numberOfSnaffles=entities-4
    SnaffleList=list() # list of ID's for the snaffles
    WizardList=list()           # list of ID's for my wizards

    for i in range(entities):
        # entity_id: entity identifier
        # entity_type: "WIZARD", "OPPONENT_WIZARD" or "SNAFFLE" (or "BLUDGER" after first league)
        # x: position
        # y: position
        # vx: velocity
        # vy: velocity
        # state: 1 if the wizard is holding a Snaffle, 0 otherwise
        entity_id, entity_type, x, y, vx, vy, state = input().split()

        if entity_type == "WIZARD":
            WizardList.append(WizardClass(int(x),int(y),int(vx),int(vy),int(state)))

        elif entity_type == "SNAFFLE":
            SnaffleList.append(SnaffleClass(int(x),int(y),int(vx),int(vy),int(state)))

    for i in range(2):
        wizard=WizardList[i]

        if wizard.state is 1:
            print("THROW" + " " + str(goalCenter[0]) + " " + str(goalCenter[1]) + " " + "500")
        else:
            location=wizard.findMyClosestSnaffleLocation(SnaffleList,numberOfSnaffles)
            print("MOVE" + " " + str(location[0]) + " " + str(location[1]) + " " + "100")

        # Write an action using print
        # To debug: print("Debug messages...", file=sys.stderr)

        # Edit this line to indicate the action for each wizard (0 ≤ thrust ≤ 150, 0 ≤ power ≤ 500)
        # i.e.: "MOVE x y thrust" or "THROW x y power"
