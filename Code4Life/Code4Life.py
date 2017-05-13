import sys
import math

class myBot(location,storage,expertise,sample_list):
    """ This is my robot """
    def __init__(self,location):
        self.hoarding = False
        self.hoarding_id = False
        self.try_connect = False
        self.location = location
        self.destination = "DIAGNOSIS"
        self.id_or_type = ""
        self.capacity = [3 10]          # carrying capacity 0:data,1:MOLECULES
        self.storage = storage
        self.my_Recipe_ids = []
        self.cloud_recipe_ids = []
        self.queue = []
        # self.expertise = expertise
        self.sample_list = sample_list

    def DIAGNOSIS_berserk(self):
        for i in range(0,self.num_open_slots("data")):
            self.queue.append("take_data")
        return "CONNECT " + str(id_of_best_recipe(self.sample_list))

    def MOLECULAR_madness(self):
        if self.hoarding

        self.queue.pop([0])
        return True

    def LABORATORY_lazarus(self):
        return True

    def exe_queue(self):

    def can_make_med(self): # needs revision ---------------------------!
        for entry in self.sample_list:
            if min([entry['cost'][i]-self.storage[i] for i in range(0,len(entry['cost'])])) >= 0 && \
             sum([entry['cost'][i]-self.storage[i] for i in range(0,len(entry['cost'])])) > 0:
                return
            else:
                return False

    def module_goto_connect(self):
        if self.destination == self.location:
            if self.destination == "laboratory":
                LABORATORY_lazarus()
            elif self.destination == "molecule" :
                MOLECULAR_madness()
            else:
                DIAGNOSIS_berserk()       #print("CONNECT " + self.id_or_type)
        else:
            print("GOTO " + self.destination)
        return True

    def num_open_slots(self,data_or_molecules):
        if data_or_molecules == "data":
            return self.capacity[0] - len(self.my_recipe_ids)
        else:
            return self.capacity[1] - len(self.storage)

    def update_recipes(self):
        self.my_recipe_ids = [entry['id'] if entry['carrier'] == 0 for entry in self.sample_list]
        self.cloud_recipe_ids = [entry['id'] if entry['carrier'] == 0 for entry in self.sample_list]
        return True

    def check_better_recipes(self):
        health_cloud_recipes = [entry['health'] if entry['carrier'] == 1 for entry in self.sample_list]
        health_my_recipes = [entry['health'] if entry['carrier'] == 0 for entry in self.sample_list]
        if max(health_cloud_recipes) > max(health_my_recipes):
            return True
        else:
            return False

# Definition of general functions
def id_of_best_recipe(recipes):
    max_health = -1
    for recipe in recipes:
        if (recipe['carrier'] == 0) && (recipe['health'] > max_health):  # if it is in the cloud
            max_health = recipe['health']
            id_best_recipe = recipe['id']
    return id_best_recipe

def needed_molecules():
    return True

# Definition of state machine
def roche_Fort_10(storage,expertise,sample_list,MyBot):
    MyBot.sample_list = sample_list #update sample_list
    MyBot.update_recipes()          #distinguish between cloud recipes and my recipes

    # Residual tasks?

    if MyBot.try_connect:
        MyBot.module_goto_connect()
        return True
    else:
        if can_make_med(sample_list,storage):
            MyBot.destination = "LABORATORY"
            MyBot.module_goto_connect()
            return True
        else:
            if MyBot.num_open_slots("molecules") > 0:
                if MyBot.check_better_recipes():
                    MyBot.DIAGNOSIS_berserk()
                    return True
            else:
                MyBot.MOLECULAR_madness()

    print(move)


# Bring data on patient samples from the diagnosis machine to the laboratory with enough molecules to produce medicine!

project_count = int(input())
for i in range(project_count):
    a, b, c, d, e = [int(j) for j in input().split()]

# game loop
while True:
    for i in range(2):
        target, eta, score, storage_a, storage_b, storage_c, storage_d, storage_e, expertise_a, expertise_b, expertise_c, expertise_d, expertise_e = input().split()
        eta = int(eta)
        score = int(score)
        storage_a = int(storage_a)
        storage_b = int(storage_b)
        storage_c = int(storage_c)
        storage_d = int(storage_d)
        storage_e = int(storage_e)
        storage = [storage_a,storage_b,storage_c,storage_d,storage_z]
        expertise_a = int(expertise_a)
        expertise_b = int(expertise_b)
        expertise_c = int(expertise_c)
        expertise_d = int(expertise_d)
        expertise_e = int(expertise_e)
        expertise = [expertise_a,expertise_b,expertise_c,expertise_d,expertise_e]

    available_a, available_b, available_c, available_d, available_e = [int(i) for i in input().split()]
    sample_count = int(input())
    sample_list = []
    for i in range(sample_count):
        sample_id, carried_by, rank, expertise_gain, health, cost_a, cost_b, cost_c, cost_d, cost_e = input().split()
        sample_id = int(sample_id)
        carried_by = int(carried_by)
        rank = int(rank)
        health = int(health)
        cost_a = int(cost_a)
        cost_b = int(cost_b)
        cost_c = int(cost_c)
        cost_d = int(cost_d)
        cost_e = int(cost_e)
        tempDict = {'id'=sample_id,'carrier'=carried_by,'rank'=rank,'health'=health,
            'cost'=[cost_a,cost_b,cost_c,cost_d,cost_e]}
        sample_list.append(tempDict)
        #print([cost_a,cost_b,cost_c,cost_d,cost_e], file=sys.stderr)

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)
