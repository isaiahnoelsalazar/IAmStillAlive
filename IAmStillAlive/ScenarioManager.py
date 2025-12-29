scenario_list = []
current_scenario = None


def start():
    with open("scenarios/scenario_list", "r") as sl:
        for s in sl.readlines():
            scenario_list.append(s.strip())


def load(camera, scenario_index = 0):
    global current_scenario
    exec(open("scenarios/" + scenario_list[scenario_index] + ".py").read(), globals(), locals())
    globals().update(locals())
    class_instance = locals()[scenario_list[scenario_index]](camera=camera)
    current_scenario = class_instance


def update():
    global current_scenario
    current_scenario.update()


def display():
    global current_scenario
    current_scenario.display()