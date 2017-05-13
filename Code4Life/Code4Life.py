import sys
import math

class myBot(location,storage,expertise,sample_list):
    """ This is my robot """
    def __init__(self,location,storage,sample_list):
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
        self.ranked_recipes = rank_recipes(self.sample_list)
        for i in range(1,self.num_open_slots("data")):
            self.queue.append("CONNECT " + str(self.rank_recipes[i]['id']))
        return "CONNECT " + str(self.rank_recipes[0]['id'])

    def MOLECULAR_madness(self):        # Horrible implementation
        self.ranked_recipes = rank_recipes(self.sample_list)
        self.can_complete = 0
        mol1 = needed_molecules(ranked_recipes[0]['cost'],self.inventory)
        tempInv = [mol1[i] + inventory[i] for i in range(0,len(inventory))]

        if num_open_slots("molecules",self.capacity,self.my_recipe_ids,tempInv) > 0:
            mol2 = needed_molecules(ranked_recipes[1]['cost'],[0, 0, 0, 0, 0])
            tempInv = [mol2[i] + tempInv[i] for i in range(0,len(inventory))]

        if num_open_slots("molecules",self.capacity,self.my_recipe_ids,tempInv) > 0:
            mol3 = needed_molecules(ranked_recipes[2]['cost'],[0, 0, 0, 0, 0])
            tempInv = [mol3[i] + tempInv[i] for i in range(0,len(inventory))]
            self.can_complete = 1
        if ~needed_molecules(ranked_recipes[2]['cost'],mol3):
            self.can_complete = 2

        molTot = [mol1[i] + mol2[i] + mol3[i] for i in rangerange(0,len(inventory))]
        for i in range(0, molTot[0]):
            self.queue.append('CONNECT ' + 'A')
        void = molTot.pop[0]

        for i in range(0, molTot[1]):
            self.queue.append('CONNECT ' + 'B')
        void = molTot.pop[1]

        for i in range(0, molTot[2]):
            self.queue.append('CONNECT ' + 'C')
        void = molTot.pop[2]

        for i in range(0, molTot[3]):
            self.queue.append('CONNECT ' + 'D')
        void = molTot.pop[3]

        for i in range(0, molTot[4]):
            self.queue.append('CONNECT ' + 'E')
        void = molTot.pop[4]

        return "CONNECT " + str(self.queue.pop[-1]) # only one molecule should remain

    def LABORATORY_lazarus(self):
        if self.can_complete >= 1:
            self.queue.append('CONNECT ' + self.ranked_recipes[1]['id'])
        if self.can_complete >= 2:
            self.queue.append('CONNECT ' + self.ranked_recipes[2]['id'])
        if self.can_complete >= 0:
            return 'CONNECT ' + self.ranked_recipes[0]['id']

    def exe_queue(self):
        return self.queue.pop[0]

    def can_make_med(self): # needs revision ---------------------------!
        for entry in self.sample_list:
            if min([entry['cost'][i]-self.storage[i] for i in range(0,len(entry['cost'])])) >= 0 && \
             sum([entry['cost'][i]-self.storage[i] for i in range(0,len(entry['cost'])])) > 0:
                return
            else:
                return False

    def module_goto_connect(self):
        if self.destination == self.location:
            if self.destination == "LABORATORY":
                return LABORATORY_lazarus()
            elif self.destination == "MOLECULE" :
                return MOLECULAR_madness()
            else:
                return DIAGNOSIS_berserk()       #print("CONNECT " + self.id_or_type)
        else:
            print("GOTO " + self.destination)
        return True

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

def rank_recipes(recipes):
    copy_recipes = recipes
    max_health = -1
    ranked_recipes = []
    for i in range(0,3):
        counter = 0
        for recipe in copy_recipes:
            if (recipe['carrier'] == 0) && (recipe['health'] > max_health):  # if it is in the cloud
                max_health = recipe['health']
                id_best_recipe = recipe['id']
                counter += 1
            ranked_recipes.append(copy_recipes.pop[counter])
    return ranked_recipes

def needed_molecules(recipe,inventory):
    ingredients = [recipe[i] - inventory[i] for i in range(0,len(inventory))]
    return ingredients

def num_open_slots(data_or_molecules,capacity,my_recipe_ids,storage):
    if data_or_molecules == "data":
        return capacity[0] - len(my_recipe_ids)
    else:
        return capacity[1] - len(storage)

# Definition of state machine
def roche_Fort_10(storage,expertise,sample_list,MyBot):
    MyBot.sample_list = sample_list #update sample_list
    MyBot.update_recipes()          #distinguish between cloud recipes and my recipes

    if len(MyBot.queue) > 0:
        move = MyBot.exe_queue()
    else:
        if MyBot.try_connect:
            move = MyBot.module_goto_connect()
        else:
            if can_make_med(sample_list,storage):
                MyBot.destination = "LABORATORY"
                move = MyBot.module_goto_connect()
            else:
                if MyBot.num_open_slots("molecules",MyBot.capacity,MyBot.my_recipe_ids,MyBot.storage) > 0:
                    if MyBot.check_better_recipes():
                        MyBot.destination = "DIAGNOSIS"
                        move = MyBot.module_goto_connect()
                else:
                    MyBot.destination = "MOLECULE"
                    move = MyBot.module_goto_connect()

    print(move)
    return True


# Initiate step counter
step_counter = 0

# Fetching the std-in stream
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

    if step_counter == 0                                                            # Is this the first tound?
        MyBot = myBot(location,storage,sample_list)                                 # Initiate Roche-Fort 1.0
    else:
        roche_Fort_10(storage,expertise,sample_list,MyBot)                          # Execute Roche-Fort 1.0


    # To debug: print("Debug messages...", file=sys.stderr)
