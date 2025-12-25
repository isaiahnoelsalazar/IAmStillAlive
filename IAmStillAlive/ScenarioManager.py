import os
import sys
import importlib

scenario_list = []
scenario_index = 0


def start(camera):
    sys.path.append(os.getcwd() + "/scenarios")
    with open(os.getcwd() + "/scenarios/scenario_list", "r") as sl:
        for s in sl.readlines():
            scenario = importlib.import_module(s.strip())
            scenario.start(camera)
            scenario_list.append(scenario)


def update():
    scenario_list[scenario_index].update()


def display():
    scenario_list[scenario_index].display()