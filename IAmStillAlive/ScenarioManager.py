import importlib

scenario_list = []
scenario_index = 0


def start(camera):
    with open("scenario_list", "r") as sl:
        for s in sl.readlines():
            scenario = importlib.import_module(s.strip())
            class_object = getattr(scenario, s.strip())
            class_instance = class_object(camera=camera)
            scenario_list.append(class_instance)


def update():
    scenario_list[scenario_index].update()


def display():
    scenario_list[scenario_index].display()