import sys
import math

class myBot(location,storage,expertise,sample_list):
    """ This is my robot """
    def __init__(self,location):
        self.hoarding = False
        self.try_connect = False
        self.location = location
        self.destination = "DIAGNOSIS"
        self.id_or_type = ""
        self.capacity = [3 10]          # carrying capacity 0:data,1:MOLECULES
        self.storage = storage
        self.expertise = expertise
        self.sample_list = sample_list

    def DIAGNOSIS_berserk:
        return True

    def MOLECULAR_madness:
        return True

    def LABORATORY_lazarus:
        return True

    def can_make_med(self): # needs revision ---------------------------!
        for entry in self.sample_list:
            if min([entry['cost'][i]-self.storage[i] for i in range(0,len(entry['cost'])])) >= 0 && \
             sum([entry['cost'][i]-self.storage[i] for i in range(0,len(entry['cost'])])) > 0:
                return
            else:
                return False

    def module_goto_connect(self):
        if self.destination == self.location:
            print("CONNECT " + self.id_or_type)
        else:
            print("GOTO " + self.destination)
        return True

    def check_open_slots(self,data_or_molecules):
        if data_or_molecules == "data":
            if self.capacity[0] > len(self.expertise):
                return True
            else:
                return False
        else:
            if self.capacity[1] > len(self.storage):
                return True
            else:
                return False

def roche_Fort_10(storage,expertise,sample_list,MyBot):
    # WIP: here needs to be an update of the bots sample_list, etc.
    #MyBot.

    if MyBot.try_connect:
        MyBot.module_goto_connect()
        return True
    else:
        if can_make_med(sample_list,storage):
            MyBot.destination = "LABORATORY"
            MyBot.module_goto_connect()
            return True
        else:
            if MyBot.check_open_slots("molecules"):



    return move


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
